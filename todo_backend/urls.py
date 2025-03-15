from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from tasks.views import ToDoViewSet

router = DefaultRouter()
router.register(r'tasks', ToDoViewSet)

urlpatterns = [
    path('api/auth/', include('authentication.urls')),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),  # Add this line
]
