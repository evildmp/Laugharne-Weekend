import os
import sys

sys.stdout = sys.stderr


#sys.path.append('/var/www/aikidocardiff')
sys.path.append('/var/www/arkestra/modules')

os.environ['DJANGO_SETTINGS_MODULE'] = 'arkestra_woodcraft.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
