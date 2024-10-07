from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import User, Staff
from .serializers import UserSerializer, StaffSerializer
from .commands import generate_auth_code


@api_view(["POST"])
def generate_code(request):
    email = request.data.get("email")
    name = request.data.get("name")

    generate_auth_code(email=email, name=name)
    return Response(
        {"message": "Auth code sent successfully"}, status=status.HTTP_200_OK
    )


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class StaffViewSet(viewsets.ModelViewSet):
    queryset = Staff.objects.prefetch_related("user").all()
    serializer_class = StaffSerializer
    lookup_field = "staff_id"

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        return Response(self.serializer_class(instance).data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = StaffSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"employee_number": serializer.data.get("staff_id")},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        serializer = StaffSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
