from django.contrib import admin
from django.urls import path, include # new
from django.conf import settings
from django.conf.urls.static import static
from app.views import Home # new

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")), # new
     path("", Home.as_view(), name="home"), # new
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)