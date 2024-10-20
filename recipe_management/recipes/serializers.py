from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Recipe

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # Explicitly include the 'id' field
        fields = ['id', 'username', 'email', 'password', 'is_staff', 'is_superuser']
        extra_kwargs = {
            'password': {'write_only': True}  # This ensures the password is write-only
        }

    # Override the create method to hash the password
    def create(self, validated_data):
        # Extract the password from validated_data
        password = validated_data.pop('password', None)
        # Create the user instance
        user = super().create(validated_data)
        # Hash the password and save the user
        if password:
            user.set_password(password)
            user.save()
        return user

    # Override the update method to hash the password
    def update(self, instance, validated_data):
        # Extract the password from validated_data
        password = validated_data.pop('password', None)
        # Update the other fields
        user = super().update(instance, validated_data)
        # Hash the password if it's present and save the user
        if password:
            user.set_password(password)
            user.save()
        return user


class RecipeSerializer(serializers.ModelSerializer):
    # Explicitly include the 'id' field
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Recipe
        # Explicitly include the 'id' field
        fields = ['id', 'title', 'description', 'ingredients', 'instructions', 'category', 'preparation_time', 'cooking_time', 'servings', 'user']
