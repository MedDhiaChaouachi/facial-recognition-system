from django.contrib import admin
from django.urls import path
from recognition_app import views  # Import your views

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin URL
    path('', views.home, name='home'),  # Home page URL
    path('recognize/', views.recognize, name='recognize'),  # Recognize endpoint
]