from django.contrib.auth.models import User, Group
from main.serializers import UserSerializer, GroupSerializer
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework import permissions
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .serializers import UserRegistrationSerializer, UserLoginSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from .models import Users, Post, Comment, Category, PostCategory, Tag 
from django.http import JsonResponse
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password, check_password

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


@api_view(['POST'])
def register_new_user(request):
    serializer = UserRegistrationSerializer(data=request.data)
    if serializer.is_valid():
        email = serializer.validated_data['email']
        uname = serializer.validated_data['username']

        if Users.objects.filter(email=email).exists():
            return Response({"error":"Email already taken"}, status=status.HTTP_409_CONFLICT)
        elif Users.objects.filter(username=uname).exists():
            return Response({"error":"Username already taken"}, status=status.HTTP_409_CONFLICT)
        
        user = serializer.save()
        return Response({"Status":"Added"}, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def login_new_user(request):
    serializer = UserLoginSerializer(data=request.data)
    
    if serializer.is_valid():
        email = serializer.data['email']
        # print(email)
        try:
            Password = list(Users.objects.filter(email=email).values())[0]['password']
            # print(Password)
            if check_password(serializer.data['password'], Password):
                return Response({"Status":"Success"}, status=status.HTTP_202_ACCEPTED)
            else:
                return Response({"Status":"Fail"}, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({"Status":"User Not Found"}, status=status.HTTP_400_BAD_REQUEST)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
