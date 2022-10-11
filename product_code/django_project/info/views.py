from django.shortcuts import render

from rest_framework import viewsets
from .serializers import InfoSerializer
from .models import Info

# Create your views here.
class InfoView(viewsets.ModelViewSet):
    serializer_class = InfoSerializer
    queryset = Info.objects.all()
