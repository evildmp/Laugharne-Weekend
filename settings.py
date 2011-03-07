# Django settings for cms project.
import os

# comment this out if you're not using LDAP; see also Authentication, below
#import ldap

PROJECT_DIR = os.path.dirname(__file__)

# ------------------------paths and urls
ROOT_URLCONF = 'arkestra-laugharne.urls'

# Absolute path to the directory that holds media.
MEDIA_ROOT = os.path.join(PROJECT_DIR, 'media/')
#ADMIN_MEDIA_ROOT = os.path.join(PROJECT_DIR, 'admin_media/')
MEDIA_URL = '/media/'

ADMIN_MEDIA_PREFIX = '/media/admin/'

FIXTURE_DIRS = [os.path.join(PROJECT_DIR, 'fixtures')]

SHOW_GENERIC_LINKS_INLINE_FOR_CMS_PAGE_ADMIN= True


DEBUG = True
TEMPLATE_DEBUG = DEBUG

# ------------------------ misc settings

SITE_ID = 1
#CACHE_BACKEND = 'locmem:///'
SECRET_KEY = 'xxxx'
INTERNAL_IPS = ('127.0.0.1',)

FILE_UPLOAD_PERMISSIONS = 0644
FILE_UPLOAD_MAX_MEMORY_SIZE = 26214400

# ------------------------  admin settings

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

# ------------------------ database settings

DATABASE_ENGINE = 'mysql'#'postgresql_psycopg2'       # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = 'xxxx'           # Or path to database file if using sqlite3.
DATABASE_USER = 'xxxx'           # Not used with sqlite3.
DATABASE_PASSWORD = 'xxxx'       # Not used with sqlite3.
DATABASE_HOST = ''     # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''              # Set to empty string for default. Not used with sqlite3.

# Test database settings
TEST_DATABASE_CHARSET = "utf8"
TEST_DATABASE_COLLATION = "utf8_general_ci"
DATABASE_SUPPORTS_TRANSACTIONS = True

# ------------------------ date and time

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be avilable on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/London'
DATE_FORMAT = "jS F Y"
TIME_FORMAT = "H\.i"

# ------------------------ languages

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
LANGUAGE_CODE = "en"
USE_I18N = True
gettext = lambda s: s

LANGUAGES = (
('en', gettext('English')),
('cy', gettext('Cymraeg')),
)

CMS_LANGUAGE_CONF = {
    'de':['fr'],
    'en':['fr'],
}

# ------------------------ Django configuration

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.core.context_processors.auth",
    "django.core.context_processors.i18n",
    "django.core.context_processors.debug",
    "django.core.context_processors.request",
    "django.core.context_processors.media",
    'django.contrib.messages.context_processors.messages',
    "cms.context_processors.media",
    "arkestra_utilities.context_processors.arkestra_templates",
)

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
    )

THUMBNAIL_SUBDIR = "output"

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',

    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
	)


TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_DIR, 'templates'),
)

INSTALLED_APPS = (
    # core Django applications

    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'django.contrib.sites',
    'django.contrib.admindocs',
    'django.contrib.messages',
    'django.contrib.humanize',

     # Django CMS applications

    'cms',
    'menus',
    'appmedia',
    'cms.plugins.text',
    'cmsplugin_filer_image',
    'cms.plugins.twitter',
    
    # Arkestra applications
    
    'contacts_and_people',
    'news_and_events',
    'links',
    'arkestra_utilities',
    'arkestra_utilities.housekeeping',
    'arkestra_utilities.admin_tabs_extension',

    # other applications
    
    'semanticeditor',
    'mptt',
    'easy_thumbnails',
    'typogrify',
    'filer',    
    'widgetry',
    'south',
)

# ------------------------ authentication

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.RemoteUserBackend',
#    'auth.ldapauth.LDAPBackend',
    'django.contrib.auth.backends.ModelBackend',
)

"""
LDAP_SERVER_URI = 'ldap://zldap1.cf.ac.uk' 
LDAP_SEARCHDN = 't=faraway' 
LDAP_SCOPE = ldap.SCOPE_SUBTREE 
LDAP_SEARCH_FILTER = 'cn=%s' 
LDAP_UPDATE_FIELDS = True 
LDAP_BIND_ATTRIBUTE = ''
LDAP_FIRST_NAME = 'givenName'
LDAP_LAST_NAME = 'sn'
LDAP_EMAIL = 'mail'
"""

AUTH_PROFILE_MODULE = 'contacts_and_people.Person'

ENABLE_CONTACTS_AND_PEOPLE_AUTH_ADMIN_INTEGRATION=True

# ------------------------ Django CMS

CMS_DEFAULT_TEMPLATE = "laugharne.html"

CMS_TEMPLATES = (
    ('arkestra.html', gettext('Arkestra')),
    ('laugharne.html', gettext('Laugharne Weekend')),

#    ('index.html', gettext('default')),
#    ('nice.html', gettext('nice one')),
#    ('cool.html', gettext('cool one')),
#    ('long-folder-long/long-template-name.html', gettext('long')),
)

CMS_APPLICATIONS_URLS = (
    ('sampleapp.urls', 'Sample application'),
    ('sampleapp.urlstwo', 'Second sample application'),
)

CMS_PLACEHOLDER_CONF = {                        
    'body': {
        "plugins": (
            'SemanticTextPlugin', 
            'CMSVacanciesPlugin', 
            'CMSNewsAndEventsPlugin', 
            'SnippetPlugin', 
            'LinksPlugin', 
            'CMSPublicationsPlugin', 
            'ImagePlugin', 
            'EntityAutoPageLinkPluginPublisher', 
            'EntityMembersPluginPublisher', 
            'FilerImagePlugin', 
            'EntityDirectoryPluginPublisher', 
            'CarouselPluginPublisher',
            'FocusOnPluginPublisher',
            'TwitterRecentEntriesPlugin',
            'TwitterSearchPlugin',
            ),
        "extra_context": {"theme":"16_5", "width":"660",},
        "name": gettext("body"),
    },
}

CMS_NAVIGATION_EXTENDERS = (('example.categories.navigation.get_nodes', 'Categories'),)
CMS_SOFTROOT = True
CMS_MODERATOR = False
CMS_PERMISSION = True
CMS_REDIRECTS = True
CMS_SEO_FIELDS = True
CMS_MENU_TITLE_OVERWRITE = True
CMS_HIDE_UNTRANSLATED = False
CMS_FLAT_URLS = False
CMS_MEDIA_URL = MEDIA_URL + 'cms/'

CMS_PAGE_FLAGS = (
    ('no_local_menu', 'Hide local menu') ,
    ('no_page_title', "Don't display page title") ,
    )

# ------------------------ Arkestra settings

ARKESTRA_BASE_ENTITY = 1 # get this wrong, and you'll be sorry
MULTIPLE_ENTITY_MODE = False
CASCADE_NEWS_AND_EVENTS = True # news & events items of children are automatically on parents' pages
MENU_MODIFIERS  = {"ArkestraPages": ("contacts", "news",)}

# heading levels

h_page_title = PAGE_TITLE_HEADING_LEVEL = 1 # global value for the heading level for page titles (e.g. entity names in entity pages)
H_MAIN_BODY = 2


# try tuple( [(i[0],u"") for i in t if i[0]<=cutoff] + [i for i in t if i[0] > cutoff] ) to generate headings
# tuple(i for i in HEADINGS if i[0] == 0 or i[0] > 2)  gives the result  ((0, u'No heading'), (3, u'Heading 3'), (4, u'Heading 4'), (5, u'Heading 5'))
HEADINGS = (
    (0, u"No heading"),
#        (1, u"Heading 1"),
    (2, u"Heading 2"),
    (3, u"Heading 3"),
    (4, u"Heading 4"),
    (5, u"Heading 5"),
    )

NEWS_AND_EVENT_LIMIT_TO = 6
# ------------------------ Semantic editor


SEMANTICEDITOR_MEDIA_URL = os.path.join(MEDIA_URL, "semanticeditor/")

# ensure that the highest_page_body_heading_level is made available below

WYM_CONTAINERS = ",\n".join([
    "{'name': 'P', 'title': 'Paragraph', 'css': 'wym_containers_p'}",
#    "{'name': 'H1', 'title': 'Heading_1', 'css': 'wym_containers_h1'}",
    "{'name': 'H2', 'title': 'Heading_2', 'css': 'wym_containers_h2'}",
    "{'name': 'H3', 'title': 'Heading_3', 'css': 'wym_containers_h3'}",
    "{'name': 'H4', 'title': 'Heading_4', 'css': 'wym_containers_h4'}",
    "{'name': 'H5', 'title': 'Heading_5', 'css': 'wym_containers_h5'}",
    "{'name': 'H6', 'title': 'Heading_6', 'css': 'wym_containers_h6'}",
#    "{'name': 'PRE', 'title': 'Preformatted', 'css': 'wym_containers_pre'}",
   "{'name': 'BLOCKQUOTE', 'title': 'Blockquote', 'css': 'wym_containers_blockquote'}",
#    "{'name': 'TH', 'title': 'Table_Header', 'css': 'wym_containers_th'}",
])

WYM_TOOLS = ",\n".join([
    "{'name': 'Bold', 'title': 'Strong', 'css': 'wym_tools_strong'}",
    "{'name': 'Italic', 'title': 'Emphasis', 'css': 'wym_tools_emphasis'}",
    "{'name': 'InsertUnorderedList', 'title': 'Unordered_List', 'css': 'wym_tools_unordered_list'}",
    "{'name': 'InsertOrderedList', 'title': 'Ordered_List', 'css': 'wym_tools_ordered_list'}",
    "{'name': 'Indent', 'title': 'Indent', 'css': 'wym_tools_indent'}",
    "{'name': 'Outdent', 'title': 'Outdent', 'css': 'wym_tools_outdent'}",
    # "{'name': 'Superscript', 'title': 'Superscript', 'css': 'wym_tools_superscript'}",
    # "{'name': 'Subscript', 'title': 'Subscript', 'css': 'wym_tools_subscript'}",
    "{'name': 'Undo', 'title': 'Undo', 'css': 'wym_tools_undo'}",
    "{'name': 'Redo', 'title': 'Redo', 'css': 'wym_tools_redo'}",
    # "{'name': 'Paste', 'title': 'Paste_From_Word', 'css': 'wym_tools_paste'}",
    "{'name': 'ToggleHtml', 'title': 'HTML', 'css': 'wym_tools_html'}",
    #"{'name': 'CreateLink', 'title': 'Link', 'css': 'wym_tools_link'}",
    #"{'name': 'Unlink', 'title': 'Unlink', 'css': 'wym_tools_unlink'}",
    #"{'name': 'InsertImage', 'title': 'Image', 'css': 'wym_tools_image'}",
    #"{'name': 'InsertTable', 'title': 'Table', 'css': 'wym_tools_table'}",
    #"{'name': 'Preview', 'title': 'Preview', 'css': 'wym_tools_preview'}",
])




# ------------------------ Links system

LINK_SCHEMA = {
    'newsarticle': {
        'search_fields': ('title',),
        'metadata_field': 'subtitle',
        'heading': 'News articles',
    },
    'person': {
        'search_fields': ('given_name','surname',),
        'heading': 'People',
    },
    'event': {
        'search_fields': ('title',),
        'metadata_field': 'subtitle',
        'heading': 'Events',
    },
    'external_link': {
        'search_fields': ('title', 'url'),
        'metadata_field': 'description',
        'heading': 'External resources',
    },
    'vacancy': {
        'search_fields': ('title',),
        'metadata_field': 'summary',
        'heading': 'Vacancies',
    },
    'page': {
        'search_fields': ('title_set__title',),
        'text_field': 'get_title',
    },
}



try:
    from local_settings import *
except ImportError:
    pass
