from rest_framework import serializers
from .models import RegisterUser

class ReisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'email', 'phoneno', 'password')
        model = RegisterUser
