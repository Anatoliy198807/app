from django.contrib import admin

from .models import Post, ProjectFile, Project
# Register your models here.

admin.site.register(Post)
admin.site.register(ProjectFile)
admin.site.register(Project)
