from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User
from src.v1.user.models.profile import Profile
from rest_framework.authtoken.models import Token
from .profile import ProfileSerializer


class UserSerializer(serializers.ModelSerializer):
    profile = serializers.SerializerMethodField()
    image = serializers.ImageField(write_only=True)
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    username = serializers.CharField(
        max_length=32,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(min_length=6, write_only=True)

    def create(self, validated_data):
        user = User(email=validated_data['email'],
                    username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        Profile.objects.create(user=user, image=validated_data['image'])
        return user

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'profile', 'image')

    @staticmethod
    def get_profile(user):
        """
        Get or create profile
        """

        profile, created = Profile.objects.get_or_create(user=user)
        return ProfileSerializer(profile, read_only=True).data

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'profile', 'image')


class UserSerializerLogin(UserSerializer):
    token = serializers.SerializerMethodField()

    @staticmethod
    def get_token(user):
        """
        Get or create token
        """

        token, created = Token.objects.get_or_create(user=user)
        return token.key

    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'profile', 'role', 'token')
