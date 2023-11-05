import os
from django.core.asgi import get_asgi_application
from decouple import config

env = config("SETTINGS")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", f"speechai.settings.{env}")
application = get_asgi_application()
