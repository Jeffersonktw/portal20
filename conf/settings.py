"""
Django settings for conf project.

Generated by 'django-admin startproject' using Django 3.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import environ
import socket # djdt for docker
from django.utils.translation import gettext_lazy as _
from corsheaders.defaults import default_headers


env = environ.Env()
root_path = environ.Path(__file__) - 2 # web

ENV = env('ENV', default='prod')
assert ENV in ['dev', 'test', 'prod', 'stag']

ROOT_URLCONF = 'conf.urls'
WSGI_APPLICATION = 'conf.wsgi.application'

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
#BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = root_path()

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

SECRET_KEY = env('SECRET_KEY')
GOOGLE_RECAPTCHA_SECRET_KEY = env('GOOGLE_RECAPTCHA_SECRET_KEY')
DEBUG = env.bool('DEBUG', default=False)

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=[])

MEDIA_URL = '/media/'
MEDIA_ROOT = env('MEDIA_ROOT', default=root_path('media'))

# Application definition

INSTALLED_APPS = [
    # default
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # first party
    'django.contrib.humanize',
    # local
    'apps.api.apps.ApiConfig',
    'apps.data.apps.DataConfig',
    'apps.article.apps.ArticleConfig',
    'apps.page.apps.PageConfig',
    # third party
    'django_ses',
    # Kuan Yu added for sitemap
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'corsheaders',
]

SITE_ID = 1

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]



CORS_ORIGIN_ALLOW_ALL = True



CORS_ALLOW_HEADERS = list(default_headers) + [
    'Access-Control-Allow-Origin',
]

CORS_ALLOW_METHODS = [
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
]
CORS_SUPPORTS_CREDENTIALS = True

ROOT_URLCONF = 'conf.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [root_path('templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
		'django.template.context_processors.i18n',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'conf.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
DATABASES = {'default': env.db('DATABASE_URL')}

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/
LANGUAGE_CODE = 'zh-Hant'

LANGUAGES = (
    ('en', ('English')),
    ('zh-hant', _('Traditional Chinese')),
)


TIME_ZONE = 'Asia/Taipei'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = env('STATIC_ROOT', default=root_path('static'))
STATICFILES_DIRS = [
    root_path('static')
]

# for djdt
if DEBUG:
    MIDDLEWARE += (
        'debug_toolbar.middleware.DebugToolbarMiddleware',
        'apps.api.middleware.DebugToolbarForJsonMiddleware'
    )
    INSTALLED_APPS += ( 'debug_toolbar',)
    #DEBUG_TOOLBAR_PANELS = (
    #    'debug_toolbar.panels.version.VersionDebugPanel',
    #    'debug_toolbar.panels.timer.TimerDebugPanel',
    #    'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
    #    'debug_toolbar.panels.headers.HeaderDebugPanel',
    #    'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
    #    'debug_toolbar.panels.template.TemplateDebugPanel',
    #    'debug_toolbar.panels.sql.SQLDebugPanel',
    #    'debug_toolbar.panels.signals.SignalDebugPanel',
    #    'debug_toolbar.panels.logger.LoggingPanel',
    #)

    # get internal ip, ex: docker
    hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
    INTERNAL_IPS = [ip[:-1] + '1' for ip in ips] + ['127.0.0.1', '10.0.2.2']

# logs
LOGS_ROOT = env('LOGS_ROOT', default=root_path('logs'))
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'console_format': {
            'format': '%(name)-12s %(levelname)-8s %(message)s %(module)s.%(funcName)s#%(lineno)d %(process)d %(thread)d'
        },
        'file_format': {
            'format': '%(asctime)s %(name)-12s %(levelname)-8s %(message)s %(module)s.%(funcName)s#%(lineno)d %(process)d %(thread)d'
        },
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s.%(funcName)s#%(lineno)d %(process)d %(thread)d %(message)s'
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'console_format'
        },
        'file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOGS_ROOT, 'django.log'),
            'maxBytes': 1024 * 1024 * 15,  # 15MB
            'backupCount': 10,
            'formatter': 'file_format',
        },
    },
    'loggers': {
        'django': {
            'level': 'INFO',
            'handlers': ['console', 'file'],
            'propagate': False,
        },
        'apps': {
            'level': 'DEBUG',
            'handlers': ['console', 'file'],
            'propagate': False,
        }
    }
}
#USE_SENTRY=on
#SENTRY_DSN=https://<project-key>@sentry.io/<project-id>

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://redis:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient"
        },
        "KEY_PREFIX": "taibif"
    }
}
# email
EMAIL_BACKEND = 'django_ses.SESBackend'
AWS_ACCESS_KEY_ID = env('AWS_ACCESS_KEY_ID', default='')
AWS_SECRET_ACCESS_KEY = env('AWS_SECRET_ACCESS_KEY', default='')
AWS_SES_REGION_NAME = env('AWS_SES_REGION_NAME', default='')
AWS_SES_REGION_ENDPOINT = env('AWS_SES_REGION_ENDPOINT', default='')

TAIBIF_SERVICE_EMAIL = env('TAIBIF_SERVICE_EMAIL', default='')
TAIBIF_BCC_EMAIL_LIST = env('TAIBIF_BCC_EMAIL_LIST', default='')

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)

