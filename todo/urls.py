from django.urls import include, path
from rest_framework import routers
from django.contrib.auth.views import LogoutView
from django.contrib.auth import logout


from . import views

router = routers.DefaultRouter()
router.register(r'tasks', views.TaskViewSet)
router.register(r'categories', views.CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

urlpatterns += router.urls
