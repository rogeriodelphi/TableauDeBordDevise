from django.contrib import admin
from django.urls import path
from devise.views import dashboard

urlpatterns = [
    path("days=<int:days_range>&currencies=<str:currencies>", dashboard),
    path('admin/', admin.site.urls),
]
