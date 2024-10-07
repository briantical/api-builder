from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from datetime import datetime
import uuid

from .models import User, Staff


@receiver(pre_save, sender=User)
def generate_username(sender, instance=None, **kwargs):
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    surname = instance.surname.replace(" ", "").lower()
    other_names = instance.other_names.replace(" ", "").lower()
    username = f"{surname}_{other_names}_{timestamp}"
    instance.username = username


@receiver(post_save, sender=Staff)
def generate_employee_number(sender, instance=None, created=False, **kwargs):
    if created:
        code = str(uuid.uuid4())[:4].upper()
        staff_id = f"EMP_{code}"
        instance.staff_id = staff_id
        instance.save()
