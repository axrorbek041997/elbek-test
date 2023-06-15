from rest_framework import serializers
from . import models


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AddressModel
        fields = '__all__'


class PitchSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PitchModel
        fields = '__all__'


class GetFreePitchSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    address_name = serializers.CharField()
    distance = serializers.FloatField()
    is_free = serializers.BooleanField()
