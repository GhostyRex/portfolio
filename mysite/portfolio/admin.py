from django.contrib import admin
from .models import Project


# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'image', 'link', 'hosted', 'created_on',)


admin.site.register(Project, ProjectAdmin)
