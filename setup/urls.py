from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from myflix.views import userViewSet, streamViewSet, listaViewSet, listaUser, listaStream
from rest_framework import routers, permissions

router = routers.DefaultRouter()
router.register('users', userViewSet, basename='users')
router.register('streams', streamViewSet, basename='streams')
router.register('listas', listaViewSet, basename='listas')

schema_view = get_schema_view(
    openapi.Info(
        title='API Documentação',
        default_version='v1',
        description='Documentação da API para o seu projeto Django',
        terms_of_service='https://www.google.com/policies/terms/',
        contact=openapi.Contact(email=''),
        license=openapi.License(name='')
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('users/<int:pk>/listas/', listaUser.as_view()),
    path('streams/<int:pk>/listas/', listaStream.as_view()),
    path('api-auth/', include('rest_framework.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
