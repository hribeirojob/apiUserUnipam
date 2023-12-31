from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.permissions import AllowAny
from rest_framework import permissions
from users.views import UserViewSet
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

schema_view = get_schema_view(
    openapi.Info(
        title="Microserviço de Usuários API",
        default_version='v1',
        description="API para gerenciamento de usuários do forum avaliativo Unipam",
        contact=openapi.Contact(email="hribeiro.job@gmail.com"),
        license=openapi.License(name="MIT"),
    ),
    public=True,
    permission_classes=(AllowAny,),  
)

urlpatterns = [
    path('', include(router.urls),),
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),

]

