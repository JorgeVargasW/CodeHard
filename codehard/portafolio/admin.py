from django.contrib import admin
from .models import UserForm

# Register your models here.

models = [UserForm]

for model in models:
    admin.site.register(model)
