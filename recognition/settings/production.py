from .base import *  # noqa

ALLOWED_HOSTS = [
    '54.159.34.159',
    '*.ermatov.me',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'recognizer',
        'USER': 'car_recognition',
        'PASSWORD': '12345!abcde@12345#',
        'HOST': 'localhost',
    }
}