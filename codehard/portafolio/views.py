from django.shortcuts import render, redirect
from .models import UserForm

# Create your views here.
def home(request):

    template = 'portafolio/home.html'

    return render(request, template)

def registerUser(request):
    template = 'portafolio/home.html'
    
    if request.method == 'POST':
        name = request.POST.get('name')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        message = request.POST.get('message')

        if name and phone_number and email and message:
            user = UserForm(
                name=name, phone_number=phone_number, email=email, message=message
            )
            user.save()
            return redirect('home')
        else:
            return render(request, template, {'error': 'Please complete all the fields'})
        
    user = UserForm.objects.all()
    context = {'user':user}

    return render(request, template, context)

