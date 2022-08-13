"""prueba URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from bienes.api.v1.bienes_views import ListBienes, BienesUpdateRetrieveDeleteView, SpecialBienesView
from users.api.v1.users_views import ListUsers, LoginView, SignInView

urlpatterns = [
    path('admin/', admin.site.urls),

    # BIENES
    path('api/v1/bienes', ListBienes.as_view(), name='bienes_api'),
    path('api/v1/bienes/<int:pk>', BienesUpdateRetrieveDeleteView.as_view(), name='bienes_api_update'),
    path('api/v1/special-bienes/', SpecialBienesView.as_view(), name='special_bienes'),

    # USERS
    path('api/v1/users', ListUsers.as_view(), name='users_api'),
    path('api/v1/signin', SignInView.as_view(), name='signin_api'),
    path('api/v1/login', LoginView.as_view(), name='login_api'),

    # JWT
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
