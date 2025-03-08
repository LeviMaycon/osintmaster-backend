from rest_framework import serializers

class ScanRequestSerializer(serializers.Serializer):
    ip = serializers.CharField(max_length=15)
    options = serializers.CharField(max_length=255)
