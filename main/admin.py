from django.contrib import admin
from . import models

admin.site.register(models.Teacher)
admin.site.register(models.Coursecategory)
admin.site.register(models.Course)
admin.site.register(models.Chapter)
admin.site.register(models.Student)
admin.site.register(models.StudentCourseEnrollment)
admin.site.register(models.CourseRating)