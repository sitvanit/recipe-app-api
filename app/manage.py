#!/usr/bin/env python
# manage.py is your tool for executing many Django-specific tasks
import os
import sys

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

# commands from the command line:

# # django-admin is Django’s command-line utility for administrative tasks.
# In addition, manage.py is automatically created in each Django project. It does the same thing as django-admin but
# also sets the DJANGO_SETTINGS_MODULE environment variable so that it points to your project’s settings.py file.
# Generally, when working on a single Django project, it’s easier to use manage.py than django-admin.
# If you need to switch between multiple Django settings files, use django-admin with DJANGO_SETTINGS_MODULE or the
# --settings command line option.

# Creates a Django project directory structure for the given project name in the current directory or the given
# destination.
# By default, the new directory contains manage.py and a project package (containing a settings.py and other files).
# docker-compose run app sh -c "django-admin.py startproject app ."

# test - Runs tests for all installed apps
# flake8 - Runs lint
# docker-compose run app sh -c "python manage.py test && flake8"

# Creates a Django app directory structure for the given app name in the current directory or the given destination.
# By default, the new directory contains a models.py file and other app template files. If only the app name is given,
# the app directory will be created in the current working directory.
# docker-compose run app sh -c "python manage.py startapp core"

