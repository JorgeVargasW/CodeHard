from django.shortcuts import render
from .models import UserForm

# Create your views here.
def home(request):
    template = 'portafolio/home.html'
    user = UserForm.objects.all()
    context = {'user':user}

    return render(request, template, context)