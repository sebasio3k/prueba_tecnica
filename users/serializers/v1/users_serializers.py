from rest_framework import serializers

from users.models import Users


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = [
            'id',
            'name',
            'username',
        ]

        extra_kwargs = {
            'id': {'read_only': True},
        }
