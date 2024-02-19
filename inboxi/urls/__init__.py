from django.contrib import admin
from django.urls import path

from inboxi.views.index import LoginView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", LoginView.as_view(), name="login")
]
