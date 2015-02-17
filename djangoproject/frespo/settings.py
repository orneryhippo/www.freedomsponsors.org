# coding: utf-8
from decimal import Decimal
from unipath import Path
import os

PROJECT_DIR = Path(__file__).parent.parent
SECRET_KEY = '*bz++cf(*#++vpo+b+=m3%p9#*x$$&amp;0mjs90x3oo5u@^zyvh)0'

FRESPO_PROJECT_ID = -1 # only needed for backwards compatibility with south patch 0008_set_isfeedback_true.py


MEDIA_ROOT = PROJECT_DIR.child('core').child('static').child('media')
MEDIA_ROOT_URL = '/static/media'

SITE_PROTOCOL = 'http'
SITE_HOST = 'localhost:8000'
SITE_NAME = 'FreedomSponsors'
SITE_HOME = SITE_PROTOCOL+'://'+SITE_HOST

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Sao_Paulo'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = ''

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = ''

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)


# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'core.middlewares.ErrorMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.transaction.TransactionMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'core.middlewares.FSPreconditionsMiddleware',
    'core.middlewares.Translation',
    'pagination.middleware.PaginationMiddleware',
    'social.apps.django_app.middleware.SocialAuthExceptionMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)


TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    'django.core.context_processors.request',
    'social.apps.django_app.context_processors.backends',
    'social.apps.django_app.context_processors.login_redirect',
    'core.context_processors.addAFewFrespoSettings',
)

ROOT_URLCONF = 'frespo.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'frespo.wsgi.application'

TEMPLATE_DIRS = (
    PROJECT_DIR.child("templates"),
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

LOCALE_PATHS = (
    PROJECT_DIR.child("locale"),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    'django.contrib.admindocs',
    'bitcoin_frespo',
    'frespo_currencies',
    'statfiles',
    'core',
    'sandbox',
    'core_splinter_tests',
    'gh_frespo_integration',
    # 'bootstrap-pagination'
    'pagination',
    'social.apps.django_app.default',
    'south',
    'emailmgr',
    'registration',
)

SOUTH_MIGRATION_MODULES = {
    'default': 'social.apps.django_app.default.south_migrations'
}


AUTHENTICATION_BACKENDS = (
    'social.backends.google.GoogleOpenId',
    'social.backends.google.GoogleOpenIdConnect',
    'social.backends.open_id.OpenIdAuth',
    'social.backends.google.GoogleOAuth2',
    'social.backends.google.GoogleOAuth',
    'social.backends.twitter.TwitterOAuth',
    'social.backends.yahoo.YahooOpenId',
    'django.contrib.auth.backends.ModelBackend',
    # 'social_auth.backends.twitter.TwitterBackend',
    # 'social_auth.backends.facebook.FacebookBackend',
    # 'social_auth.backends.google.GoogleOAuthBackend',
    # 'social_auth.backends.google.GoogleOAuth2Backend',
    # 'social_auth.backends.google.GoogleBackend',
    # 'social_auth.backends.yahoo.YahooBackend',
    # 'social_auth.backends.OpenIDBackend',

    # 'social_auth.backends.contrib.linkedin.LinkedinBackend',
#    'social_auth.backends.contrib.skyrock.SkyrockBackend',
#     'social_auth.backends.contrib.flickr.FlickrBackend',
#     'social_auth.backends.contrib.instagram.InstagramBackend',
#     'social_auth.backends.contrib.github.GithubBackend',
#     'social_auth.backends.contrib.bitbucket.BitbucketBackend',
#     'social_auth.backends.contrib.yandex.YandexBackend',
#    'social_auth.backends.contrib.yahoo.YahooOAuthBackend',
#     'social_auth.backends.contrib.livejournal.LiveJournalBackend',
#    'social_auth.backends.contrib.douban.DoubanBackend',
#     'social_auth.backends.browserid.BrowserIDBackend',
#    'social_auth.backends.contrib.vkontakte.VKontakteBackend',
#    'social_auth.backends.contrib.yandex.YandexOAuth2Backend',
#     'social_auth.backends.contrib.yandex.YaruBackend',
#    'social_auth.backends.contrib.odnoklassniki.OdnoklassnikiBackend',
#    'social_auth.backends.contrib.vkontakte.VKontakteOAuth2Backend',
#    'social_auth.backends.contrib.mailru.MailruBackend',
#     'django.contrib.auth.backends.ModelBackend',
)

TEST_GMAIL_ACCOUNT_1 = {
    'username' : 'eunemqueriaessacontamesmo',
    'password' : 'blimblom',
}
TEST_GMAIL_ACCOUNT_2 = {
    'username' : 'minhaoutracontafake',
    'password' : 'blimblom',
}


SOCIAL_AUTH_PROTECTED_USER_FIELDS = ['email',]
FACEBOOK_EXTENDED_PERMISSIONS = ['email',]
#GITHUB_EXTENDED_PERMISSIONS = ['public_repo']
GITHUB_EXTENDED_PERMISSIONS = []


LOGIN_URL          = '/login'
LOGIN_REDIRECT_URL = '/'
GITHUB_EXTRA_DATA = [('login', 'social_username')]
FACEBOOK_EXTRA_DATA = [('username', 'social_username')]
TWITTER_EXTRA_DATA = [('screen_name', 'social_username')]

ACCOUNT_ACTIVATION_DAYS = 1

LOGIN_ERROR_URL = '/login-error/'
SOCIAL_AUTH_INACTIVE_USER_MESSAGE = 'This account has been deactivated'

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.

PAGINATION_DEFAULT_PAGINATION = 20
PAGINATION_DEFAULT_WINDOW = 3

##############################################################
# settings that are likely to change on different environments
# ############################################################

ALLOWED_HOSTS = ['localhost']
ADMINS = (
    ('Admin', 'admin@freedomsponsors.org'),
)
MANAGERS = ADMINS

DEBUG = True
TEMPLATE_DEBUG = DEBUG

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

SKIPTESTS_TRACKERINTEGRATION = False # Skip tests in tests_trackerintegration
SKIPTESTS_BITCOINADAPTER = True
SKIPTESTS_PAYPALAPI = True
SKIPTESTS_ACCOUNTGMAIL = True

FS_FEE = Decimal('0.03')
BITCOIN_FEE = Decimal('0.0002')
FETCH_ISSUE_TIMEOUT = 10.0
SECRET_KEY = '*bz++cf(*#++vpo+b+=m3%p9#*x$$&amp;0mjs90x3oo5u@^zyvh)0'
ENABLE_PIWIK = False

GITHUB_BOT_USERNAME = 'freedomsponsors-bot'
GITHUB_BOT_PASSWORD = '*********'

PAYPAL_USE_SANDBOX = True
PAYPAL_DEBUG = False
PAYPAL_IPNNOTIFY_URL_TOKEN = 'megablasteripn'
PAYPAL_API_USERNAME = "FP_1338073142_biz_api1.gmail.com"
PAYPAL_API_PASSWORD = '1338073168'
PAYPAL_API_SIGNATURE = 'AFcWxV21C7fd0v3bYYYRCpSSRl31AVAvZTYca4potYVRXAbpeSKQGHZO'
PAYPAL_API_APPLICATION_ID = 'APP-80W284485P519543T' #see www.x.com
PAYPAL_API_EMAIL = 'FP_1338073142_biz@gmail.com'
PAYPAL_FRESPO_RECEIVER_EMAIL = 'FP_1338073142_biz@gmail.com'

PAYPAL_CANCEL_URL = SITE_HOME+'/core/paypal/cancel'
PAYPAL_RETURN_URL = SITE_HOME+'/core/paypal/return'
PAYPAL_IPNNOTIFY_URL = SITE_HOME+'/core/paypal/'+PAYPAL_IPNNOTIFY_URL_TOKEN

BITCOIN_IPNNOTIFY_URL_TOKEN = 'megablasteripn'
BITCOIN_ENABLED = False
BITCOIN_RECEIVE_ADDRESS_POOL_SIZE = 20

MOCK_OPENEXCHANGE_RATES = True
# OPENEXCHANGERATES_API_KEY = '01ac624c42df447aa14a80f5844ee1d3'

TWITTER_CONSUMER_KEY         = ''
TWITTER_CONSUMER_SECRET      = ''
FACEBOOK_APP_ID              = ''
FACEBOOK_API_SECRET          = ''
LINKEDIN_CONSUMER_KEY        = ''
LINKEDIN_CONSUMER_SECRET     = ''
ORKUT_CONSUMER_KEY           = ''
ORKUT_CONSUMER_SECRET        = ''
GOOGLE_CONSUMER_KEY          = ''
GOOGLE_CONSUMER_SECRET       = ''
GOOGLE_OAUTH2_CLIENT_ID      = ''
GOOGLE_OAUTH2_CLIENT_SECRET  = ''
SOCIAL_AUTH_GOOGLE_OPENIDCONNECT_KEY = 'XXXXX'
SOCIAL_AUTH_GOOGLE_OPENIDCONNECT_SECRET = 'XXXXX'
FOURSQUARE_CONSUMER_KEY      = ''
FOURSQUARE_CONSUMER_SECRET   = ''
GITHUB_APP_ID                = ''
GITHUB_API_SECRET            = ''
DROPBOX_APP_ID               = ''
DROPBOX_API_SECRET           = ''
FLICKR_APP_ID                = ''
FLICKR_API_SECRET            = ''
INSTAGRAM_CLIENT_ID          = ''
INSTAGRAM_CLIENT_SECRET      = ''
VK_APP_ID                    = ''
VK_API_SECRET                = ''
BITBUCKET_CONSUMER_KEY       = ''
BITBUCKET_CONSUMER_SECRET    = ''
LIVE_CLIENT_ID               = ''
LIVE_CLIENT_SECRET           = ''
SKYROCK_CONSUMER_KEY         = ''
SKYROCK_CONSUMER_SECRET      = ''
YAHOO_CONSUMER_KEY           = ''
YAHOO_CONSUMER_SECRET        = ''

if os.getenv('USE_TEST_DB') == '1':
    DATABASES = {
        # 'default': dj_database_url.config(
        #     default='sqlite:///' + PROJECT_DIR.child('database.db'))
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'frespotesting',
            'USER': 'frespo',
            'PASSWORD': 'frespo',
            'HOST': 'localhost',
            'PORT': '5432',
            'TEST_MIRROR': 'default',
        }
    }
else:
    DATABASES = {
        # 'default': dj_database_url.config(
        #     default='sqlite:///' + PROJECT_DIR.child('database.db'))
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'frespo',
            'USER': 'frespo',
            'PASSWORD': 'frespo',
            'HOST': 'localhost',
            'PORT': '5432',
            # 'TEST_MIRROR': None,
        }
    }


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'null': {
            'level':'DEBUG',
            'class':'django.utils.log.NullHandler',
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'default': {
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': PROJECT_DIR.child('logs', 'frespo.log'),
            'maxBytes': 1024*1024*5, # 5 MB
            'backupCount': 5,
            'formatter':'standard',
        },
    },
    'loggers': {
        '': {
            'handlers': ['default'],
            'level': 'DEBUG',
            'propagate': True
        },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django.db': {
            'handlers': ['null'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
