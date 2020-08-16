Django Admin Tool Command
=========================

![image](https://travis-ci.org/daadu/django-admintool-command.svg?branch=master%0A%20:target:%20https://travis-ci.org/daadu/django-admintool-command)

A reusable Django app that allows to run mangement commands from admin
site

Installation
------------

To get the latest stable release from PyPi

    pip install django-admintool-command

To get the latest commit from GitHub

    pip install -e git+git://github.com/daadu/django-admintool-command.git#egg=admintool_command

TODO: Describe further installation steps (edit / remove the examples
below):

Follow installation instructions for
<https://github.com/django-admin-tools/django-admin-tools>

Add `admintool_command` to your `INSTALLED_APPS`

    INSTALLED_APPS = (
        ...,
        'admin_tools',
        'admin_tools.menu',
        'admin_tools.dashboard',
        'admintool_command',
    )

Add the `admintool_command` URLs to your `urls.py`

    urlpatterns = [
        url(r'^admin/commands/', include('admintool_command.urls')),
    ]

Usage
-----

Commands need to inherit from admintool\_command.AdminCommand and
implement at least a Form which is used to present the command
arguments.

Then these are added to settings like:

    ADMIN_TOOLS_COMMANDS = {
        'app_name': ['command_name'],
    }

Optionally, add admintool\_command.dashboards.AdminCommandMenu to your
django-admin-tools menu.

TODO: Describe about django-admin-tools

TODO: Describe usage or point to docs. Also describe available settings
and templatetags.

Contribute
----------

If you want to contribute to this project, please perform the following
steps

    # Fork this repository
    # Clone your fork
    virtualenv -p python3.6 venv
    source venv/bin/activate
    make develop

    git co -b feature_branch master
    # Implement your feature and tests
    git add . && git commit
    git push -u origin feature_branch
    # Send us a pull request for your feature branch

In order to run the tests, simply execute `tox`. This will install four
new environments (for Django 1.11, 2.0, 2.1 and 2.2) and run the tests
against all environments.
