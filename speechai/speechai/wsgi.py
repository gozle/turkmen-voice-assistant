import os
from django.core.wsgi import get_wsgi_application
from decouple import config

env = config("ENVIRONMENT")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", f"speechai.settings.{env}")
application = get_wsgi_application()
