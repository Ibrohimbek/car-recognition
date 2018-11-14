import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'n#6f8%xk*hdw-syh(efjrw0%_6jqj5dpyuakxh*!nso4*-p%kl'

DEBUG = False

ADMINS = [
    ('Ibrohim Ermatov', 'ibrohimbek@gmail.com'),
]

ALLOWED_HOSTS = [
    '*',
]

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',

    'recognition',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.common.CommonMiddleware',
]

ROOT_URLCONF = 'recognition.api.urls'

WSGI_APPLICATION = 'recognition.wsgi.application'

# Internationalization
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_PAGINATION_CLASS':
        'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 100,
    'ORDERING_PARAM': 'ordering',
}
