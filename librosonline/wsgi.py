import os
import sys

# Ruta al directorio del proyecto en PythonAnywhere
path = '/home/flor-p/DJANGO-AVANZADO_proyecto-final_agosto-2025'
if path not in sys.path:
    sys.path.append(path)

# Nombre del módulo de settings de Django
os.environ["DJANGO_SETTINGS_MODULE"] = "librosonline.settings"

# Aplicación WSGI
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()