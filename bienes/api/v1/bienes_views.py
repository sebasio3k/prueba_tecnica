from django.http import JsonResponse
from rest_framework import generics
from rest_framework.response import Response

from bienes.models import Bienes
from bienes.serializers.v1.bienes_serializers import BienesSerializer
from users.models import Users
from users.serializers.v1.users_serializers import UserSerializer


class ListBienes(generics.ListCreateAPIView):
    queryset = Bienes.objects.all()
    serializer_class = BienesSerializer

    # permission_classes = [IsAdminUser]

    def create(self, request, *args, **kwargs):

        serializer = self.get_serializer(
            data=request.data,
            context=
            {
                'usuario': Users.objects.get(id=request.data.get('usuario_id'))
            }
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return JsonResponse(serializer.errors, status=422)


class BienesUpdateRetrieveDeleteView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BienesSerializer
    queryset = BienesSerializer.Meta.model.objects

    def update(self, request, pk=None, *args, **kwargs):
        print(f'llave: {pk}')
        instance = self.serializer_class.Meta.model.objects.get(pk=pk)
        print('data', request.data)

        updated = self.serializer_class(
            instance,
            data=request.data,
            context={
                'usuario': Users.objects.get(id=request.data.get('usuario_id'))
            }
        )

        if updated.is_valid():
            updated.save()
            return JsonResponse(updated.data, status=200)
        else:
            return JsonResponse(updated.errors, status=200)


class SpecialBienesView(generics.ListAPIView):
    # queryset = Bienes.objects.all()
    serializer_class = BienesSerializer

    def get_queryset(self):

        # Get URL parameter as a string, if exists
        ids = self.request.query_params.get('ids', None)
        print('ids', ids)

        # Get snippets for ids if they exist
        if ids is not None:
            print('if')
            # Convert parameter string to list of integers
            ids = [int(x) for x in ids.split(',')]
            # Get objects for all parameter ids
            queryset = Bienes.objects.filter(pk__in=ids)
            print(queryset)

        else:
            print('else')
            # Else no parameters, return all objects
            queryset = Bienes.objects.all()

        return queryset
