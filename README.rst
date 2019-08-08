Django Admin Tool Command
=========================

.. image:: https://travis-ci.org/daadu/django-admintool-command.svg?branch=master
    :target: https://travis-ci.org/daadu/django-admintool-command

A reusable Django app that allows to run mangement commands from admin site

Installation
------------

To get the latest stable release from PyPi

.. code-block:: bash

    pip install django-admintool-command

To get the latest commit from GitHub

.. code-block:: bash

    pip install -e git+git://github.com/daadu/django-admintool-command.git#egg=admintool_command

TODO: Describe further installation steps (edit / remove the examples below):

Add ``admintool_command`` to your ``INSTALLED_APPS``

.. code-block:: python

    INSTALLED_APPS = (
        ...,
        'admintool_command',
    )

Add the ``admintool_command`` URLs to your ``urls.py``

.. code-block:: python

    urlpatterns = [
        url(r'^admin/commands/', include('admintool_command.urls')),
    ]




Usage
-----
TODO: Describe about django-admin-tools

TODO: Describe usage or point to docs. Also describe available settings and
templatetags.


Contribute
----------

If you want to contribute to this project, please perform the following steps

.. code-block:: bash

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

In order to run the tests, simply execute ``tox``. This will install four new
environments (for Django 1.11, 2.0, 2.1 and 2.2) and run the tests against all
environments.
