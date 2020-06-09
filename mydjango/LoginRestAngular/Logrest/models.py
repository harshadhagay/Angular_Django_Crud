from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    username=models.CharField(max_length=20)
    name=models.CharField(max_length=20)
    address=models.CharField(max_length=45)
    email=models.EmailField(unique=True)
    image=models.ImageField(null=True)
    
