from django.contrib import admin
from django.urls import path
from pages.views import landing

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landing, name='landing'),
]
