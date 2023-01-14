from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Users


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class UserRegistrationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Users
        fields = ['name','email', 'username', 'password', 'created_at', 'updated_at']

class UserLoginSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Users
        fields = ['email','password']
    