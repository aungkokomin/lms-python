from django.db import models

class Lesson(models.Model):
    module = models.ForeignKey('Module', on_delete=models.CASCADE, related_name='lessons')
    title = models.CharField(max_length=100)
    contents = models.TextField(blank=True, null=True)
    status = models.CharField(choices=[('draft','Draft'),('published','Published'),('archived','Archived')], max_length=20, default='draft')
    sorting_order = models.PositiveIntegerField(default=1, help_text="Determines the order of lessons within a module")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title
