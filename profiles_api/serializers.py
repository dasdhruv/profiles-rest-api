from rest_framework import serializers
from profiles_api import models

class HelloSerializer(serializers.Serializer):
    """ serializes a name field for testing our APIView """
    username = serializers.CharField(max_length = 12)


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserProfile
        fields = ('id','email','name', 'password')
        extra_kwargs = {'password':
                                    {'write_only':True, 'style':{'input_type':'password'}
                                    }
                          }
        print("I am in Meta class")

    def create(this, validated_data):
        user = models.UserProfile.objects.create_user(email = validated_data['email'], name = validated_data['name'], password = validated_data['password'])
        return user
