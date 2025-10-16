from django.contrib import admin

from .models import Affiliate, Bundle, Course, CourseBundle, Lesson, Module, Student

# Register your models here.
admin.site.site_header = "LMS Admin"
admin.site.site_title = "LMS Admin Portal"
admin.site.index_title = "Welcome to LMS Admin Portal"
admin.site.register([Affiliate, Bundle, Course, CourseBundle, Lesson, Module, Student])