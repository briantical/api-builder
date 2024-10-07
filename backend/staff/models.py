import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser


class BaseModel(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    _created_at = models.DateTimeField(auto_now_add=True, editable=False)
    _modified_at = models.DateTimeField(auto_now=True, db_index=True)

    class Meta:
        abstract = True
        ordering = ["_modified_at"]


class User(AbstractUser, BaseModel):
    date_of_birth = models.DateField(blank=False, null=False)
    email = models.EmailField(unique=True, blank=True, null=True)
    surname = models.CharField(max_length=255, blank=False, null=False)
    other_names = models.CharField(max_length=255, blank=False, null=False)

    def __str__(self):
        return f"{self.surname} {self.other_names}"


class Staff(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    staff_id = models.CharField(max_length=255, blank=True, null=True)
    id_photo = models.ImageField(upload_to="staff/images", blank=True, null=True)

    def __str__(self):
        return f"{self.user.surname} {self.user.other_names}"


class AuthCode(BaseModel):
    code = models.CharField(max_length=10)
    is_active = models.BooleanField(default=True)

    @staticmethod
    def generate_unique_code():
        while True:
            code = str(uuid.uuid4())[:10].upper()
            if not AuthCode.objects.filter(code=code, is_active=True).exists():
                return code

    def __str__(self):
        return "User authorization code"
