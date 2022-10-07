from itertools import permutations
from rest_framework import generics,permissions
from . import serializer
from . import models

class VendorList(generics.ListCreateAPIView):
    queryset=models.Vendor.objects.all()
    serializer_class= serializer.VenderSerializer
    # permission_classes= [permissions.IsAuthenticated]


class VendorDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset=models.Vendor.objects.all()
    serializer_class= serializer.VenderDetailSerializer
    # permission_classes= [permissions.IsAuthenticated]