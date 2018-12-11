from django.shortcuts import render

# Create your views here.
from rest_framework.generics import CreateAPIView

from Admin.serializers import AdminUserSerializer


class AdminUserAPIView(CreateAPIView):
    serializer_class = AdminUserSerializer