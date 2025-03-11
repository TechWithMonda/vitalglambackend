import os
import django
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "your_project.settings")

django.setup()

# Run migrations on startup
from django.core.management import call_command
call_command("migrate")

application = get_wsgi_application()
