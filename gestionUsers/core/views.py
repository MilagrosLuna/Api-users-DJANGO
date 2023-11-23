from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import UserSerializer, UserSerializerCreate


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return UserSerializerCreate
        return UserSerializer

