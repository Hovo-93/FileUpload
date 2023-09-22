from .models import *
from rest_framework import serializers


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ('id', 'file', 'uploaded_at')


class FileListSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = '__all__'
