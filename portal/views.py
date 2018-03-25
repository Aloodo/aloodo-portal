from django.http import HttpResponse
from django.template import loader

def profile(request):
    template = loader.get_template('profile.html')
    context = {}
    return HttpResponse(template.render(context, request))
