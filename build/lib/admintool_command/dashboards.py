from admin_tools.dashboard import modules
from admin_tools.menu.items import MenuItem
from admin_tools.utils import AppListElementMixin
from django.conf import settings
from django.urls import reverse
from django.utils.safestring import mark_safe

from admintool_command.utils import get_command_instance


class AdminCommandMenu(MenuItem, AppListElementMixin):
    title = "Commands"

    def init_with_context(self, context):

        for app_name, commands in settings.ADMIN_TOOLS_COMMANDS.items():
            children = []
            for command in commands:
                instance = get_command_instance(app_name, command)

                title = mark_safe(instance.name if instance.name else "%s" % command)
                url = reverse("admintool_command:command", kwargs={"app_name": app_name, "command": command})

                children.append(MenuItem(title=title, url=url))
            self.children.append(MenuItem(app_name, children=children))

        if not len(self.children):
            self.enabled = False

    def is_selected(self, request):
        return False


class AdminCommandModule(modules.Group):
    title = "Commands"

    enabled = True
    display = "stacked"

    def init_with_context(self, context):
        for app_name, commands in settings.ADMIN_TOOLS_COMMANDS.items():
            children = []
            for command in commands:
                instance = get_command_instance(app_name, command)

                children.append({'title': mark_safe(instance.name if instance.name else command),
                                 'url': reverse("admintool_command:command",
                                                kwargs={"app_name": app_name, "command": command})
                                 })

            self.children.append(modules.LinkList(title=app_name, draggable=False, children=children))

    def is_empty(self):
        return len(self.children) == 0
