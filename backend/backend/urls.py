from django.contrib import admin
from django.urls import path, include

from staff.urls import urlpatterns as staff_urls

api_urls = [
    path("staff/", include(staff_urls)),
]
urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(api_urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
