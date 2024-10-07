from django.urls import path, include


from rest_framework import routers

from .views import StaffViewSet, generate_code

router = routers.DefaultRouter()
router.register(r"", StaffViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("code", generate_code),
]
