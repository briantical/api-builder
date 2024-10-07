from rest_framework import serializers
from .models import User, Staff, AuthCode


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["date_of_birth", "email", "surname", "other_names"]


class StaffSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    authorization_code = serializers.CharField(
        write_only=True, required=True, max_length=10
    )

    class Meta:
        model = Staff
        fields = ["staff_id", "id_photo", "user", "authorization_code"]

        read_only_fields = ("staff_id",)

    def create(self, validated_data):
        auth_code = validated_data.pop("authorization_code")
        codes = AuthCode.objects.filter(code=auth_code, is_active=True)

        if not codes.exists():
            raise serializers.ValidationError(
                {"authorization_code": "Invalid authorization code"}
            )

        user_data = validated_data.pop("user")
        user = User.objects.create(**user_data)
        staff = Staff.objects.create(user=user, **validated_data)

        instance = codes.first()
        instance.is_active = False
        instance.save()

        return staff
