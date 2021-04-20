from rest_framework import serializers
from django.utils.translation import gettext_lazy as _
from .models import User


class SignUpSerializer(serializers.ModelSerializer):
    """用户注册序列化器"""
    email_push = serializers.BooleanField(label=_('email push'), default=False, write_only=True)

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'password',
            'email_push'
        ]
        extra_kwargs = {
            "username": {
                "min_length": 5,
                "max_length": 32,
                "error_messages": {
                    "mix_length": "用户名长度区间5-32",
                    "max_length": "用户名长度区间5-32",
                }
            },
            "password": {
                "min_length": 8,
                "max_length": 32,
                "error_messages": {
                    "mix_length": "密码长度区间8-32",
                    "max_length": "密码长度区间8-32",
                }
            }
        }
