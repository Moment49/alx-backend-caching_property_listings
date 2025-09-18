from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Property


class RegisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ["username", "email", "password", "confirm_password"]
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, data):
        """ Validate the password and confirm password"""  
        password = data.get('password')
        confirm_password = data.get('confirm_password')

        if len(password) < 5 and confirm_password < 5:
            raise serializers.ValidationError("Password must be above 5 characters long")
        if password != confirm_password:
            raise serializers.ValidationError("Sorry passwords must match")
        return data

    def create(self, validated_data):
        password = validated_data.pop('password')
        # Hash the password
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)

class PropertySerializer(serializers.ModelSerializer):
    model = Property
    fields = ['id', 'title', 'description', 'price', 'location']
    read_only_fields = ['id']
    
