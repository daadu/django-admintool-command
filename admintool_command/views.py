import traceback
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.messages.storage.base import Message
from django.core.management import call_command
from django.http import HttpResponse
from django.shortcuts import render
from django.utils.safestring import mark_safe
from django.views import View
from io import StringIO

from admintool_command.utils import get_command_instance, colourstrip


class AppCommandView(UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user and self.request.user.is_superuser

    def get(self, request, app_name, command):
        instance = get_command_instance(app_name, command)
        # handle from AdminCommand if has view handler
        if hasattr(instance, "view"):
            return instance.view(request=request, app_name=app_name, command=command)

        context = instance.init_context(request=request, app_name=app_name, command=command)
        context["title"] = mark_safe(instance.name if instance.name else "%s" % command)
        context["app_name"] = app_name
        context["form"] = instance.Form()
        return HttpResponse(render(request, instance.template, context=context))

    def post(self, request, app_name, command):
        instance = get_command_instance(app_name, command)
        # handle from AdminCommand if has view handler
        if hasattr(instance, "view"):
            return instance.view(request=request, app_name=app_name, command=command)

        form = instance.Form(request.POST)
        context = instance.init_context(request=request, app_name=app_name, command=command)
        context["title"] = mark_safe(instance.name if instance.name else "%s" % command)
        context["app_name"] = app_name
        context["form"] = form
        if form.is_valid():
            args, options = instance.get_command_arguments(forms_data=form.cleaned_data)
            output = StringIO()
            extra_tags = ""
            try:
                call_command(command, stdout=output, no_color=True, *args, **options)
            except Exception as e:
                output.write(traceback.format_exc())
                output.seek(0)
                extra_tags = "error"
            message = colourstrip(output.getvalue().replace("\n", '<br/>')) if output.getvalue() else "Done"
            context["messages"] = [
                Message(level=0, extra_tags=extra_tags, message=message)]
            return HttpResponse(render(request, instance.template, context=context))
        context["messages"] = [Message(level=0, extra_tags="error", message="Invalid form data")]
        return HttpResponse(render(request, instance.template, context=context))
