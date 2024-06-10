from django.contrib import admin
from .models import *

# Register your models here.
class projectimageinline(admin.TabularInline):
    model = ProjectImage
    extra = 1

class Projectadmin(admin.ModelAdmin):
    list_display = ("title","link")
    inlines = [projectimageinline]
    search_fields = ("title", "description")
    list_filter = ("tags",)

class tagadmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)

admin.site.register(Project, Projectadmin)
admin.site.register(ProjectImage)
admin.site.register(Tag, tagadmin)