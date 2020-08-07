from django import forms

from .command import AdminCommand

def get_full_class_name(app_name, command):
    return "%s.management.commands.%s.Command" % (app_name, command)


def get_command_instance(app_name, command):
    full_class_name = get_full_class_name(app_name, command)
    module_name = full_class_name.split(".")
    class_name = module_name.pop()

    from importlib import import_module
    _module = import_module(".".join(module_name))
    _class = getattr(_module, class_name)

    instance = _class()
    if isinstance(instance, AdminCommand):
        return instance

    setattr(instance, "name", command)
    setattr(instance, "Form", forms.Form)
    setattr(instance, "template", "admintool_command/command.html")
    setattr(instance, "init_context", lambda *args, **kwargs: {})
    setattr(instance, "get_command_arguments", lambda *args, **kwargs: ([], {}))
    return instance


def colourstrip(data):
    while True:
        find = data.find('\x1b')
        if find <= -1:
            break
        data = data[:find] + data[find + 5:]
        find = data.find('\x1b')
        data = data[:find] + data[find+4:]
    data = data.replace("[31m", "")
    return data.strip()
