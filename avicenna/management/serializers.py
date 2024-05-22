from rest_framework import serializers
from management.models import *


class ProfileMeta:
    exclude = ["password"]
    read_only_fields = ["username", "user_type", "created_at", "updated_at", "last_login", "date_joined"]


class UserSerializer(serializers.ModelSerializer):

    """User model serializer"""

    class Meta(ProfileMeta):
        model = User





class ChangePasswordSerializer(serializers.Serializer):

    """Change password serializer"""

    password = serializers.CharField(write_only=True)
    new_password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)
