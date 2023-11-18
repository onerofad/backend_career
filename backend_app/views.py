from django.shortcuts import render
from rest_framework import viewsets
from .models import RegisterUser
from .serializer import ReisterUserSerializer

class RegisterUserView(viewsets.ModelViewSet):
    queryset = RegisterUser.objects.all()
    serializer_class = ReisterUserSerializer
