from django.db import models

# Create your models here.
class UserForm(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self) -> str:
        return self.name    