from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "accounts/login/",
        LoginView.as_view(template_name="registration/login.html"),
        name="login",
    ),
    path(
        "accounts/logout/",
        LogoutView.as_view(next_page="/"),
        name="logout",
    ),
    path("", include("taxi.urls", namespace="taxi")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
