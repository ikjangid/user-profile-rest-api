from rest_framework import serializers

class MySerializers(serializers.Serializer):
    """Serializers a name fieeld for testing our APIView"""

    name = serializers.CharField(max_length=10)