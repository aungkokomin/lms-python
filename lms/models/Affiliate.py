from django.db import models

class Affiliate(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    affiliate_uuid = models.CharField(max_length=10, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField(blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

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

