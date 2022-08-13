from rest_framework import serializers

from bienes.models import Bienes
from users.models import Users
from users.serializers.v1.users_serializers import UserSerializer


class BienesSerializer(serializers.ModelSerializer):
    usuario_detail = serializers.SerializerMethodField('get_user', read_only=True)

    def get_user(self, obj):
        try:
            qs = Users.objects.get(id=obj.usuario.id)
            return UserSerializer(qs).data
        except:
            return []

    def create(self, validated_data):
        validated_data['usuario_id'] = self.context.get('usuario').id
        return Bienes.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.articulo = validated_data.get('articulo', instance.articulo)
        instance.descripcion = validated_data.get('descripcion', instance.descripcion)
        instance.usuario_id = self.context.get('usuario').id
        instance.save()
        return instance

    class Meta:
        model = Bienes
        fields = [
            'id',
            'articulo',
            'descripcion',
            'usuario_id',
            'usuario_detail',
        ]

        extra_kwargs = {
            'id': {'read_only': True},
        }
