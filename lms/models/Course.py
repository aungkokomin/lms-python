from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=100, help_text="Title of the course")
    description = models.TextField( blank=True, null=True, help_text="Detailed description of the course")
    price = models.DecimalField(max_digits=6, decimal_places=2, help_text="Price of the course in USD")
    is_active = models.BooleanField(default=True, help_text="Designates whether this course is active")
    validity_period = models.IntegerField(help_text="Validity period in days")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title