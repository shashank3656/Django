

import sys, os, django

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.insert(0, BASE_DIR)


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "webbloging.settings")

os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
 
django.setup()