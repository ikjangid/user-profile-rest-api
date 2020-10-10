from rest_framework import serializers

from user_profile_api import models


class MySerializers(serializers.Serializer):
    """Serializers a name fieeld for testing our APIView"""

    name = serializers.CharField(max_length=10)


class ProfileSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""
    
    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    def create(self, validated_data):
        """Create and return a new user"""
        user = models.UserProfile.objects.create_user(
            email = validated_data['email'],
            name = validated_data['name'],
            password = validated_data['password']
        )

        return user