from django.urls import include, path
from rest_framework import routers
from . import views



router = routers.DefaultRouter()
router.register(r'tasks', views.TaskViewSet)
router.register(r'categories', views.CategoryViewSet)

from rest_framework.authtoken import views as auth_views


urlpatterns = [
    path('', include(router.urls)),
    path('register/', views.UserCreateView.as_view(), name='register'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-token-auth/', auth_views.obtain_auth_token)
]

urlpatterns += router.urls 
