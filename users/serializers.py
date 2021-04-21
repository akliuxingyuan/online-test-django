from rest_framework import serializers
from .models import User


class SignUpSerializer(serializers.ModelSerializer):
    """用户注册序列化器"""

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email',
            'password',
        )
        extra_kwargs = {
            "username": {
                "min_length": 4,
                "max_length": 32,
                "error_messages": {
                    "mix_length": "用户名长度区间5-32",
                    "max_length": "用户名长度区间5-32",
                }
            },
            "password": {
                "min_length": 6,
                "max_length": 32,
                "error_messages": {
                    "mix_length": "密码长度区间8-32",
                    "max_length": "密码长度区间8-32",
                }
            }
        }

    def create(self, validated_data):
        """
        创建用户
        """
        user = super().create(validated_data)

        # 调用django的认证系统加密密码
        user.set_password(validated_data['password'])
        user.save()

        return user
