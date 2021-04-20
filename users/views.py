from django.shortcuts import render

# Create your views here.
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import SignUpSerializer
from .models import User


class UserSignUpView(CreateAPIView):
    """用户注册"""

    serializer_class = SignUpSerializer


class UserExistView(APIView):
    """判断用户是否存在"""

    def get(self, request, username):
        count = User.objects.filter(username=username).count()
        data = {
            "username": username,
            "exist": count
        }
        return Response(data)
