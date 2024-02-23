"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 5.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
import os
import environ

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# .env file, should load only in development environment
env = environ.Env()
READ_DOT_ENV_FILE = env.bool('DJANGO_READ_DOT_ENV_FILE', default=True)
if READ_DOT_ENV_FILE:
    env_file = os.path.join(BASE_DIR, ".env")
    print('Loading : {}'.format(env_file))
    env.read_env(env_file)
    print('The .env file has been loaded. See base.py for more information')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'django-insecure--xgjt(*0geto9)4+a==kh54boh4jr!mr2(p*bxq3fw(#gp-*fq'
SECRET_KEY = os.environ['DJANGO_SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool('DJANGO_DEBUG', False)

# Djangoへのアクセスを許可するホスト
try:
    ALLOWED_HOSTS = os.environ['DJANGO_ALLOWED_HOSTS'].split(',')
except KeyError as e:
    ALLOWED_HOSTS = ['*']

# Application definition
INSTALLED_APPS = [
    # 'jazzmin'
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
INSTALLED_APPS += [
    'users.apps.UsersConfig',
    'api.apps.ApiConfig'
]
if DEBUG:
    INSTALLED_APPS += [
        'django_extensions',
        'debug_toolbar',
    ]

AUTH_USER_MODEL = 'users.User'

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',   # for CROS
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
if DEBUG:
    MIDDLEWARE += [
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    ]
else:
    # Django DRF GUIのコンソールを非表示
    REST_FRAMEWORK = { 
        'DEFAULT_RENDERER_CLASSES': (
            'rest_framework.renderers.JSONRenderer',
        ),
    }

# django-jazzmin
# https://django-jazzmin.readthedocs.io/configuration/
# JAZZMIN_SETTINGS = {
#     # title of the window (Will default to current_admin_site.site_title if absent or None)
#     "site_title": "app",
# 
#     # Title on the login screen (19 chars max) (defaults to current_admin_site.site_header if absent or None)
#     "site_header": "app",
# 
#     # Title on the brand (19 chars max) (defaults to current_admin_site.site_header if absent or None)
#     # "site_brand": "Library",
# 
#     # Logo to use for your site, must be present in static files, used for brand on top left
#     #"site_logo": "books/img/logo.png",
# 
#     # Logo to use for your site, must be present in static files, used for login form logo (defaults to site_logo)
#     # "login_logo": None,
# 
#     # Logo to use for login form in dark themes (defaults to login_logo)
#     #"login_logo_dark": None,
# }

# POSTのCSRFドメインを指定
# https://docs.djangoproject.com/en/4.0/ref/settings/#csrf-trusted-origins
try:
    CSRF_TRUSTED_ORIGINS = os.environ['DJANGO_CSRF_TRUSTED_ORIGINS'].split(',')
except KeyError as e:
    CSRF_TRUSTED_ORIGINS = []

# クライアントのCORSを指定
if DEBUG:
    # アクセスを許可したいURL（アクセス元）
    try:
        CORS_ORIGIN_WHITELIST = os.environ['DJANGO_CORS_ORIGIN_WHITELIST'].split(',')
    except KeyError as e:
        # 全てを許可
        CORS_ORIGIN_ALLOW_ALL = True
    # レスポンスを公開する. 自身以外のオリジンのHTTPリクエスト内にクッキーを含めることを許可する
    CORS_ALLOW_CREDENTIALS = True
    # 許可するメソッドを指定する
    CORS_ALLOW_METHODS = [
        'DELETE',
        'GET',
        'OPTIONS',
        'PATCH',
        'POST',
        'PUT',
    ]
    # 許可するヘッダーを指定する
    CORS_ALLOW_HEADERS = [
        'accept',
        'accept-encoding',
        'authorization',
        'content-type',
        'dnt',
        'origin',
        'user-agent',
        'x-csrftoken',
        'x-requested-with',
    ]
else:
    # アクセスを許可したいURL（アクセス元）
    try:
        CORS_ORIGIN_WHITELIST = os.environ['DJANGO_CORS_ORIGIN_WHITELIST'].split(',')
    except KeyError as e:
        CORS_ORIGIN_WHITELIST = []   # ex. CORS_ORIGIN_WHITELIST = ['http://localhost:3000']
    # レスポンスを公開する. 自身以外のオリジンのHTTPリクエスト内にクッキーを含めることを許可する
    CORS_ALLOW_CREDENTIALS = True
    # プリフライト(事前リクエスト)の設定
    # 30分だけ許可
    CORS_PREFLIGHT_MAX_AGE = 60 * 30

ROOT_URLCONF = 'config.urls'

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

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

# for sqlite3
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# for postgres
# DATABASES = {
#    'default': {
#        'ENGINE': os.environ['POSTGRES_ENGINE'],
#        'NAME': os.environ['POSTGRES_DB'],
#        'USER': os.environ['POSTGRES_USER'],
#        'PASSWORD': os.environ['POSTGRES_PASSWORD'],
#        'HOST': os.environ['POSTGRES_HOST'],
#        'PORT': os.environ['POSTGRES_PORT']
#    }
# }


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

# LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'ja-jp'
# TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Tokyo'
USE_I18N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, "dist")
STATIC_URL = 'static/'
# static/ ディレクトリのリスト
"""
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'node_modules'),
)
"""

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# --------------------------------------------------
# LOGGING
# --------------------------------------------------
LOGGING_PATH = os.path.join(BASE_DIR, 'logs')
LOGGING_FILE = 'app.log'
LOGGING_API_FILE = 'api.log'

if os.name == 'nt':
    LOGGING = {
        'version': 1,   # これを設定しないと怒られる
        'formatters': {
            'all': {
                'format': ':'.join([
                    "[%(levelname)s]",
                    "%(asctime)s",
                    "%(process)d",
                    "%(thread)d",
                    "%(message)s",
                ])
            },
        },
        'handlers': {
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'formatter': 'all',
            }
        },
        'loggers': {  # loggerの名前を定義
            'app': {
                'handlers': ['console'],
                'level': 'DEBUG',
            },
            'api': {
                'handlers': ['console'],
                'level': 'DEBUG',
            },
        },
    }

else:
    LOGGING = {
        'version': 1,
        'formatters': {
            'all': {
                'format': ':'.join([
                    "[%(levelname)s]",
                    "%(asctime)s",
                    "%(process)d",
                    "%(thread)d",
                    "%(message)s",
                ])
            },
        },
        'handlers': {
            'file_no_rotation': {
                'level': 'DEBUG',
                'class': 'logging.FileHandler',
                'filename': os.path.join(LOGGING_PATH, LOGGING_FILE),
                'formatter': 'all',
            },
            'file_size_rotation': {
                'level': 'DEBUG',
                'class': 'logging.handlers.RotatingFileHandler',
                'filename': os.path.join(LOGGING_PATH, LOGGING_FILE),
                'formatter': 'all',
                'maxBytes': 1024 * 1024,
            },
            'file_time_rotation': {
                'level': 'DEBUG',
                'class': 'logging.handlers.TimedRotatingFileHandler',
                'filename': os.path.join(LOGGING_PATH, LOGGING_FILE),
                'formatter': 'all',
                'when': 'D',
                'interval': 1,
            },
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'formatter': 'all',
            },
            'file_time_rotation_api': {
                'level': 'DEBUG',
                'class': 'logging.handlers.TimedRotatingFileHandler',
                'filename': os.path.join(LOGGING_PATH, LOGGING_API_FILE),
                'formatter': 'all',
                'when': 'D',
                'interval': 1,
            }
        },
        'loggers': {
            'app': {
                'handlers': ['file_time_rotation', 'console'],
                'level': 'DEBUG',
            },
            'api': {
                'handlers': ['file_time_rotation_api', 'console'],
                'level': 'DEBUG',
            },
        },
    }

# --------------------------------------------------
# GDAL settings for Windows
# --------------------------------------------------
import os
if os.name == 'nt':
    import platform
    POSTGRES = env.str("DJANGO_WINDOWS_POSTGRES", default=r"C:\PostgreSQL\15")
    OSGEO4W = env.str("DJANGO_WINDOWS_OSGEO4W", default=r"C:\QGIS\2.18")
    assert os.path.isdir(OSGEO4W), "Directory does not exist: " + OSGEO4W

    os.environ['OSGEO4W_ROOT'] = OSGEO4W
    os.environ['POSTGRES_ROOT'] = POSTGRES
    os.environ['GDAL_LIBRARY_PATH'] = OSGEO4W + r"\bin"
    os.environ['GEOS_LIBRARY_PATH'] = OSGEO4W + r"\bin"
    os.environ['PATH'] = OSGEO4W + r"\bin;" + POSTGRES + r"\bin;" + os.environ['PATH']

    GDAL_LIBRARY_PATH = env.str("DJANGO_GDAL_LIBRARY_PATH", default=r"")
