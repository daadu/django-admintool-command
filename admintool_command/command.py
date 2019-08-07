from abc import ABC, abstractmethod

from django import forms
from django.core.management import BaseCommand


class AdminCommand(BaseCommand, ABC):
    name = None
    template = "admintool_command/command.html"

    class Form(forms.Form):
        pass

    def init_context(self, request=None, **kwargs):
        return dict()

    @abstractmethod
    def get_command_arguments(self, forms_data):
        pass
