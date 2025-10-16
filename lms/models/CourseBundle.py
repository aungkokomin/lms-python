from django.db import models

class CourseBundle(models.Model):
    course = models.ForeignKey('Course', on_delete=models.CASCADE, related_name='course_bundles')
    bundle = models.ForeignKey('Bundle', on_delete=models.CASCADE, related_name='course_bundles')
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    # price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name