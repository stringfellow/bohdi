from models import *
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, get_host, HttpResponse
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.conf import settings

from shutil import copytree,rmtree,move
from os.path import abspath, dirname, join
from datetime import datetime

from cStringIO import StringIO
import zipfile
import os

#from django.contrib.gis.utils import mapping,ogrinspect

from pprint import pprint

from django.db.models import get_model,get_models,get_app
#from django.contrib.gis.utils import LayerMapping

from django.contrib.sites.models import Site


def user_body(request,username):
    """
        render out the user's body info page
    """
    
    user = get_object_or_404(User,pk=0)
    
    return render_to_response("user_body.html",{'theuser':user},context_instance=RequestContext(request))
