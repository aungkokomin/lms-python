import uuid

from django.db import models

class Affiliate(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    affiliate_uuid = models.CharField(max_length=30, unique=True, verbose_name="Affiliate ID")
    first_name = models.CharField(max_length=30, verbose_name="First Name")
    last_name = models.CharField(max_length=30, verbose_name="Last Name")
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField(blank=True, null=True, verbose_name="Date of Birth")
    phone_number = models.CharField(max_length=15, blank=True, null=True, verbose_name="Phone Number")
    address = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True, verbose_name="Active")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    # class Meta:
    #     verbose_name = "Affiliate"
    #     verbose_name_plural = "Affiliates"
    #     ordering = ['-created_at']
    #     indexes = [
    #         models.Index(fields=['affiliate_uuid']),
    #         models.Index(fields=['email']),
    #     ]
    #     constraints = [
    #         models.UniqueConstraint(fields=['email'], name='unique_affiliate_email')
    #     ]
    #     permissions = [
    #         ("view_affiliate", "Can view affiliate"),
    #         ("add_affiliate", "Can add affiliate"),
    #         ("change_affiliate", "Can change affiliate"),
    #         ("delete_affiliate", "Can delete affiliate"),
    #     ]

