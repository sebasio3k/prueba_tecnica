from django.contrib.auth import authenticate
from django.http import JsonResponse
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import AccessToken

from users.models import Users
from users.serializers.v1.users_serializers import UserSerializer


class ListUsers(generics.ListCreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class SignInView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        name = request.data.get('name', None)
        username = request.data.get('username', None)
        password = request.data.get('password', None)
        password_confirm = request.data.get('password_confirm', None)

        # password confirm validation
        if password != password_confirm:
            return JsonResponse({
                "error": "La contraseña no coincide",
                "field": "password_confirm"
            }, status=422)

        serializer = UserSerializer(data={
            'name': name,
            'username': username,
            'password': password,
        })

        if serializer.is_valid():
            account = serializer.save()
            account.set_password(password)
            account.save()

            return JsonResponse({
                "token": str(AccessToken().for_user(account))
            }, status=200)

        else:
            return JsonResponse({
                "error": "No se puede realizar su registro",
                "detail": serializer.errors
            }, status=422)


class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username', None)
        password = request.data.get('password', None)

        if username is None:
            return JsonResponse({
                "error": "Nombre de usuario invalido",
                "field": "username"
            }, status=422)

        if password is None:
            return JsonResponse({
                "error": "Contraseña invalida",
                "field": "password"
            }, status=422)

        # LOGIN
        user = authenticate(request, username=username, password=password)
        print(user)

        # User exists?
        exists = Users.objects.filter(username=username).exists()
        if user is not None:
            return JsonResponse({
                "token": str(AccessToken().for_user(user))
            }, status=200)

        else:
            if exists:
                return JsonResponse({
                    "error": "Contraseña incorrecta",
                    "field": "password"
                }, status=422)
            else:
                return JsonResponse({
                    "error": "Esta usuario no esta registrada",
                    "field": "username"
                }, status=422)
