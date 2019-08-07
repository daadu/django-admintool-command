from django.urls import path

from .views import AppCommandView

app_name = 'admintool_command'
urlpatterns = [
    path(r'<str:app_name>/<str:command>/', AppCommandView.as_view(), name="command"),
]
