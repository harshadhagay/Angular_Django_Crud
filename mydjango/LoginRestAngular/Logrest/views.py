from django.shortcuts import render
from .serializers import UserSerilizer
from .models import UserProfile
from rest_framework.generics import RetrieveUpdateDestroyAPIView,ListCreateAPIView

# Create your views here.
class Userdata(RetrieveUpdateDestroyAPIView):
    queryset=UserProfile.objects.all()
    serializer_class=UserSerilizer
class Userdatalist(ListCreateAPIView):
    queryset=UserProfile.objects.all()
    serializer_class=UserSerilizer

