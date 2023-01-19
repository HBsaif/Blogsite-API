from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Users, Post, Comment


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class UserLoginSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Users
        fields = ['email','password']

class PostCreateSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.PrimaryKeyRelatedField(queryset=Users.objects.all())
    class Meta:
        model = Post
        fields = ['title','body', 'author']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"

class PostViewSerializer(serializers.ModelSerializer):
    commemt = CommentSerializer(many=True, read_only=True)
    class Meta:
        model = Post
        fields = "__all__"
        # fields = ['post_id', 'title', 'body', 'author', 'created_at', 'updated_at', 'published_at', 'status']


class UserRegistrationSerializer(serializers.ModelSerializer):
    # posts = PostViewSerializer(many=True, read_only=True)
    posts = serializers.StringRelatedField(many=True)
    user_comment = CommentSerializer(many=True, read_only=True)
    class Meta:
        model = Users
        # fields = ['name','email', 'username', 'created_at', 'updated_at', 'posts', 'commemt']
        fields = "__all__"