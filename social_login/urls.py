from django.contrib import admin
from django.urls import path, include # new

from app.views import Home # new

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")), # new
     path("", Home.as_view(), name="home"), # new
]