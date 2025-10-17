import uuid

from django.db import models

class Student(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    student_uuid = models.CharField(max_length=30, unique=True ,verbose_name="Student ID")
    first_name = models.CharField(max_length=30, verbose_name="First Name")
    last_name = models.CharField(max_length=30, verbose_name="Last Name")
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField(blank=True, null=True, verbose_name="Date of Birth")
    phone_number = models.CharField(blank=True, null=True, max_length=15, verbose_name="Phone Number")
    address = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True, verbose_name="Active")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # deleted_at = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"