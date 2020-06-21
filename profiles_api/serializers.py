from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """ serializes a name field for testing our APIView """
    username = serializers.CharField(max_length = 12)
