# -*- encoding: utf-8 -*-
import os
import json


""" * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
Árbol de Directorios
"""
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC_ROOT = os.getenv('APPSXSALUD2016_STATIC_ROOT', os.path.join(BASE_DIR, "static"))
MEDIA_ROOT = os.getenv('APPSXSALUD2016_MEDIA_ROOT', os.path.join(BASE_DIR, "media"))


""" * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
Administracion
"""
ADMINS = (
    ("Martin Josemaria", "martin.vuelta@gmail.com"),
)


""" * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
Seguridad
"""

SECRET_KEY = os.getenv("APPSXSALUD2016_SECRET_KEY", "5Up3r*53CR3T*k3y")

DEBUG = json.loads(os.getenv("APPSXSALUD2016_DEBUG_SITE", "true"))

ALLOWED_HOSTS = os.getenv("APPSXSALUD2016_TEMPLATE_DEBUG", "*").split(":")

SECURE_PROXY_SSL_HEADER = ("APPSXSALUD2016_HTTP_X_FORWARDED_PROTO", "https")


""" * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
Aplicaciones
"""
INSTALLED_APPS = [
    'material',
    'material.admin',

    # Default
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # third-party
    'captcha',
    'overextends',
    'rest_framework',

    # Own
    'module_dni',
    'module_hospital',
    'module_ambulance',
    'module_fingerprint',
]


""" * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
Middlewares
"""
MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


""" * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
Configuracion de direcciones (URLs)
"""
STATIC_URL = os.getenv("APPSXSALUD2016_STATIC_URL", "/static/")
MEDIA_URL = os.getenv("APPSXSALUD2016_MEDIA_URL", "/media/")
ROOT_URLCONF = 'appsxsalud2016.urls'


""" * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
Pantillas
"""
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'builtins': ['overextends.templatetags.overextends_tags'],
            'debug': json.loads(os.getenv("APPSXSALUD2016_DEBUG_TEMPLATES", "true")),
        },
    },
]


""" * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
Aplicacionde WSGI
"""
WSGI_APPLICATION = 'appsxsalud2016.wsgi.application'


""" * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
Bases de Datos
"""
DATABASES = {
    'default': {
        "ENGINE": os.getenv("APPSXSALUD2016_DB_ENGINE", "django.db.backends.sqlite3"),
        "NAME": os.getenv("APPSXSALUD2016_DB_NAME", os.path.join(BASE_DIR, "db.sqlite3")),
        "USER": os.getenv("APPSXSALUD2016_DB_USER", ""),
        "PASSWORD": os.getenv("APPSXSALUD2016_DB_PASSWORD", ""),
        "HOST": os.getenv("APPSXSALUD2016_DB_HOST", ""),
        "PORT": os.getenv("APPSXSALUD2016_DB_PORT", ""),
    }
}


""" * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
Password validation
"""
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


""" * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
Internationalizacion y localizacion
"""
LANGUAGE_CODE = 'es-es'
TIME_ZONE = os.getenv("APPSXSALUD2016_TIME_ZONE", "America/Lima")
USE_I18N = True
USE_L10N = True
USE_TZ = True


""" * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
Otros Ajustes
"""
# Google Maps
GOOGLE_MAPS_API_KEY = os.getenv("GOOGLE_API_KEY", "")

# Google ReCapthcha
RECAPTCHA_PUBLIC_KEY = os.getenv("GOOGLE_RECAPTCHA_PUBLIC_KEY", "")
RECAPTCHA_PRIVATE_KEY = os.getenv("GOOGLE_RECAPTCHA_PRIVATE_KEY", "")
RECAPTCHA_USE_SSL = True
NOCAPTCHA = True
