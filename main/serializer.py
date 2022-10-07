from rest_framework import serializers
from . import models

class VenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Vendor
        fields=['user','address']
    def __init__(self, *args, **kwargs):
        super(VenderSerializer,self).__init__(*args, **kwargs)
        self.Meta.depth = 1

class VenderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Vendor
        fields=['id','user','address']
    def __init__(self, *args, **kwargs):
        super(VenderDetailSerializer,self).__init__(*args, **kwargs)
        self.Meta.depth = 1