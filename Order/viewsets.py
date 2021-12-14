from rest_framework import viewsets
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from . import models
from . import serializers

class OrderViewset(viewsets.ModelViewSet):
	queryset = models.Order.objects.all()
	serializer_class = serializers.OrderSerializer
