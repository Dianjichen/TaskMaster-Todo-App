from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from tasks.views import ToDoViewSet  # ✅ Import correctly
from django.http import HttpResponse

router = DefaultRouter()
router.register(r'tasks', ToDoViewSet)  # ✅ Correct usage

def home(request):
    return HttpResponse("Welcome to the Task API!")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home),  # Default home route to avoid 404
    path("api/", include("tasks.urls")),  # ✅ This ensures API routes work
]
