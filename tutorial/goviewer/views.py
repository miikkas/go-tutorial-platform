from django.http import HttpResponse, HttpResponseNotFound
from django.template import Context, loader

from goviewer.models import *

def index(request):
    """
    The root page for go tutorial viewer. Shows the user the
    front screen of the JavaScript application.
    """
    template = loader.get_template("goviewer/index.html")
    context = Context({
        "" : None,
    })
    return HttpResponse(template.render(context))

