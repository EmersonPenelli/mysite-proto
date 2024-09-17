
"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

<<<<<<< HEAD
application = get_wsgi_application()
=======
application = get_wsgi_application()

>>>>>>> 895054c95ba3ad15c15d45832ada295a566627af
