from decouple import config
from speechai.utils import EnvironmentSettings
from speechai.settings.base import (
    AUTH_PASSWORD_VALIDATORS,
    ROOT_URLCONF,
    TEMPLATES,
    BASE_DIR,
)

settings_instance = EnvironmentSettings()
BASE_DIR = BASE_DIR
ROOT_URLCONF = ROOT_URLCONF

SECRET_KEY = settings_instance.secret_key
DEBUG = settings_instance.debug

ALLOWED_HOSTS = config(
    "ALLOWED_HOSTS_DEV", cast=lambda v: [s.strip() for s in v.split(",")]
)

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    )
}

INSTALLED_APPS = [
    "speech_api",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "corsheaders",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "speechai.urls"


WSGI_APPLICATION = "speechai.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}



# try:
#     DATABASES = {
#         "default": {
#             "ENGINE": "django.db.backends.postgresql",
#             "HOST": settings_instance.database_settings["host"],
#             "NAME": settings_instance.database_settings["database"],
#             "USER": settings_instance.database_settings["username"],
#             "PASSWORD": settings_instance.database_settings["password"],
#             "PORT": settings_instance.database_settings["port"],
#         }
#     }

# except EnvironmentError:
#     from speechai.settings.base import DATABASE_LITE

#     DATABASES = DATABASE_LITE

AUTH_PASSWORD_VALIDATORS = AUTH_PASSWORD_VALIDATORS
TEMPLATES = TEMPLATES
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True
DATETIME_FORMAT = "%Y-%m-%d %H:%M"
DATETIME_INPUT_FORMATS = "%Y-%m-%d %H:%M"
STATIC_URL = "ASR_OUTPUT/"
