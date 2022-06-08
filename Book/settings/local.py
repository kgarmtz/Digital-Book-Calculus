from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=True, cast=bool)

# ALLOWED_HOSTS = ['polilibro-env.eba-ad2fmztg.us-west-2.elasticbeanstalk.com', '*']
ALLOWED_HOSTS = ['book-app-env.eba-ipvdkpmb.us-west-2.elasticbeanstalk.com', '*']

# CORS_ALLOWED_ORIGINS = [
#     'https://polilibrocalculo.com',
#     'http://localhost:8080',
#     'http://127.0.0.1:8000',
# ] 

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

import os

# If the project is beign executed on the AWS Cloud then use this configuration 
if 'RDS_DB_NAME' in os.environ:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.environ['RDS_DB_NAME'],
            'USER': os.environ['RDS_USERNAME'],
            'PASSWORD': os.environ['RDS_PASSWORD'],
            'HOST': os.environ['RDS_HOSTNAME'],
            'PORT': os.environ['RDS_PORT'],
        }
    }

# Otherwise, use this configuration (local server)
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR.child('db.sqlite3'),
        }
    } 
 
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

# STATIC_URL = '/static/'

# # Defining the static files directory : BASE_DIR / 'static' 
# # where Django will find all the necessary statics files
STATICFILES_DIRS = [BASE_DIR.child('static')]

# AWS S3 Static Files Configuration

# All the images will be uploaded in this path when we 
# register a new one in the Django Admin Panel
MEDIA_URL = '/media/'

# Directory that will hold all the user-uploaded files
MEDIA_ROOT = BASE_DIR.child('media')  

# Ckeditor settings
CKEDITOR_UPLOAD_PATH = 'uploads/'
CKEDITOR_IMAGE_BACKEND = 'pillow' 
CKEDITOR_JQUERY_URL = 'https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js'
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['Bold', 'Italic', 'Underline'],
            ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
            ['TextColor', 'Format', 'FontSize', 'Link'],
            ['Smiley', 'Image', 'Iframe'],
            ['RemoveFormat', 'Source']
        ],
        'removePlugins': 'stylesheetparser',
        'allowedContent': True,
    }
}



