"""
WSGI config for workTest project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""
# activate_this = '/home/djangotest/env/bin/activate_this.py'
# execfile(activate_this, dict(__file__=activate_this))

import os
import sys

from django.core.wsgi import get_wsgi_application

path = 'home/Warkb/WorkTest'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'workTest.settings'
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "workTest.settings")

application = get_wsgi_application()
