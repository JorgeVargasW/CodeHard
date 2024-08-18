from django.shortcuts import render

# Create your views here.
def home(request):
    template = 'portafolio/home.html'

    return render(request, template)