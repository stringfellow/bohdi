from django.contrib.auth.models import User
from body.build_templates import *


try:
    User.objects.get(username="steve")
except:
    User.objects.create_superuser("steve", "steve@synfinity.net", "wibble")

addBones()
addBoneSurfaces()
#addMuscles()


