from rest_framework import serializers
from .models import all_user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = all_user
        fields = ['name', 'dob', 'email', 'phone_no']