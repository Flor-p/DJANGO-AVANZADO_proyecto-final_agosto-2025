import os
import sys

# Agrega la ruta del proyecto al path
path = '/var/www/librosonline'
if path not in sys.path:
    sys.path.append(path)

# Establece la configuración de Django
os.environ["DJANGO_SETTINGS_MODULE"] = "librosonline.settings"

# Carga la aplicación WSGI de Django
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

