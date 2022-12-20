from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
from Fuel_UR_Way.models import  Car
User = get_user_model()

# Authentications Serializers ..


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    access = serializers.CharField(allow_blank=True, read_only=True)

    class Meta:
        model = User
        fields = ["id", "access", "username", "password"]
      

    def create(self, validated_data):
        username = validated_data["username"]
        password = validated_data["password"]
        new_user = User(username=username)
        new_user.set_password(password)
        new_user.save()
 
        payload = RefreshToken.for_user(new_user)
        token = str(payload.access_token)

        validated_data["access"] = token
        print("Successfully Created An Acount ")  #to test

        return validated_data


class SigninSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    access = serializers.CharField(allow_blank=True, read_only=True)

    def validate(self, data):
        print(data)
        username = data.get("username")
        password = data.get("password")

        try:
            user = User.objects.get(username=username)

        except User.DoesNotExist:
            raise serializers.ValidationError("User Does Not Exist!!")
        if not user.check_password(password):
            raise serializers.ValidationError("Incorrect Password")

        payload = RefreshToken.for_user(user)
        payload["username"] = user.username
        token = str(payload.access_token)
        data["username"] = user.username

        data["access"] = token
        return data

# Category Serializer ..



class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['id','carType', 'fuleType', 'owner']
        

class CarUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['carType', 'fuleType', 'owner']

