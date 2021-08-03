from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True #Ver errores de developer(por seguridad se deshabilita)

ALLOWED_HOSTS = ['djangoblogdateam.herokuapp.com']


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'deuo99fuiqglkn',
        'USER':'bylbrnkfsdtgqv',
        'PASSWORD':'b1292940c6628a2c6b072510521ff08c9a7f56ab459587d44aa0ff6b8516161d',
        'HOST':'ec2-54-196-65-186.compute-1.amazonaws.com',
        'PORT':5432,
    }
}

STATICFILES_DIRS = (BASE_DIR,'static')
