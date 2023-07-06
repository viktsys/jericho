# Python imports
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent                           # jericho
PROJECT_BASE_DIR = Path(__file__).resolve().parent.parent.parent            # app
REPOSITORY_BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent  # jericho (GIT)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-hjb@ftm_t@$ka*vgl6b0139%o(g8ix!ikl(phi59l$ksepfz98"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# 
ALLOWED_HOSTS = []


# Application definition
INSTALLED_APPS = [
    # Django (Base)
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # Rest Framework
    "rest_framework",

    # ViteJS
    "django_vite",

    # Project
    "core",
    "app"
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

ROOT_URLCONF = "jericho.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [PROJECT_BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]
WSGI_APPLICATION = "jericho.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True


# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/
STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "collectedstatic"

# Django Vite
# https://github.com/MrBin99/django-vite
DJANGO_VITE_ASSETS_PATH = REPOSITORY_BASE_DIR / "app" / "static" / "dist"
DJANGO_VITE_DEV_SERVER_PROTOCOL = "http"
DJANGO_VITE_DEV_SERVER_HOST = "127.0.0.1"
DJANGO_VITE_DEV_SERVER_PORT = 3000
DJANGO_VITE_DEV_MODE = DEBUG

#
STATICFILES_DIRS = [DJANGO_VITE_ASSETS_PATH]