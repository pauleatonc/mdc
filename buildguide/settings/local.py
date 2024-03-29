from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-local-secret-key-should-be-unique-and-secret'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '*']

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases
# Adjust the database settings for your local development environment
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mdc',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static",]

# Media files
# Defines the base URL and directory to serve user uploaded files during development
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / "media"

# Email Backend
# Configure a local email backend if necessary, for development purposes
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Logging
# Customize logging for local development if needed
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'WARNING', #cambiar a debug para más logs
            'propagate': True,
        },
    },
}
