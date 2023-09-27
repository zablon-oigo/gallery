from django.contrib import admin
from .models import Category, Photo

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display=['category','name','slug','image','created_by']
    list_filter=['created_at','updated_at','created_by']
    prepopulated_fields={'slug':('name',)}
    date_hierarchy='created_at'
    ordering=['created_at',]

admin.site.register(Category)
# admin.site.register(Photo)

