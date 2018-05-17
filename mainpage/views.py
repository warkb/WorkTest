from django.template import RequestContext, loader
from django.http import HttpResponse

# Create your views here.
def index(request):
    template = loader.get_template('mainpage/authpage.html')
    return HttpResponse(template.render())
