from django.contrib import admin
from .models import Category, MediaFile
# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(MediaFile)
class MediaFileAdmin(admin.ModelAdmin):
    list_display = ('file', 'media_type', 'category')