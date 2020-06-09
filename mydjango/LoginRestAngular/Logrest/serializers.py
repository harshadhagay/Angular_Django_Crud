from rest_framework import serializers
from .models import UserProfile
class UserSerilizer(serializers.ModelSerializer):
    class Meta:
        model=UserProfile
        fields=('username','name','address','email','image')