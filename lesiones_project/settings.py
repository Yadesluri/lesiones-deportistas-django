from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent


# ============================
#       CONFIGURACIÓN BASE
# ============================

SECRET_KEY = os.getenv("SECRET_KEY", "django-insecure-proyecto-lesiones")
DEBUG = os.getenv("DEBUG", "True") == "True"

ALLOWED_HOSTS = []


# ============================
#     APLICACIONES INSTALADAS
# ============================

INSTALLED_APPS = [
    # Django Base Apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Apps del proyecto
    'app_lesiones',
    'cuentas',
]


# ============================
#          MIDDLEWARE
# ============================

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# ============================
#            URLs
# ============================

ROOT_URLCONF = 'lesiones_project.urls'


# ============================
#          TEMPLATES
# ============================

# Agregamos BASE_DIR / 'templates' para poder usar un base.html global
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
        },
    },
]


# ============================
#            WSGI
# ============================

WSGI_APPLICATION = 'lesiones_project.wsgi.application'


# ============================
#         BASE DE DATOS
# ============================

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'lesiones_db',
        'USER': 'root',
        'PASSWORD': 'admin',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}


# ============================
#      IDIOMA / TIMEZONE
# ============================

LANGUAGE_CODE = 'es-es'
TIME_ZONE = 'America/Santiago'

USE_I18N = True
USE_TZ = True


# ============================
#           ESTÁTICOS
# ============================

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')


# ============================
#     LOGIN / LOGOUT CONFIG
# ============================

LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'panel'
LOGOUT_REDIRECT_URL = 'login'


# ============================
#     CONTROL DE SESIÓN
# ============================

SESSION_COOKIE_AGE = 1800  # 30 min
SESSION_SAVE_EVERY_REQUEST = True


# ============================
#    MENSAJES BOOTSTRAP
# ============================

from django.contrib.messages import constants as messages

MESSAGE_TAGS = {
    messages.ERROR: 'danger',
    messages.SUCCESS: 'success',
    messages.INFO: 'info',
    messages.WARNING: 'warning',
}


# ============================
#    CONFIGURACIÓN SEGURIDAD
# ============================

CSRF_COOKIE_SECURE = False
SESSION_COOKIE_SECURE = False
X_FRAME_OPTIONS = 'DENY'
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True


# ============================
#       AUTOINCREMENT
# ============================

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
