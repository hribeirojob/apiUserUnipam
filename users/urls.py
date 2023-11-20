from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from users.views import UserViewSet

urlpatterns = [
    path('', UserViewSet.as_view({'get': 'list', 'post': 'create'}), name='user-list'),
    path('<int:pk>/', UserViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='user-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
