from .models import AppUser
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppUser
        fields = ['name', 'email', 'password', 'is_superuser']
        extra_kwargs = {
            'password': {'write_only': True},
            'is_superuser': {'write_only': True}
        }
    def create(self, validated_data):
        user = AppUser.objects.create_user(**validated_data)
        return user