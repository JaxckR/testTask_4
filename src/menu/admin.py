from django.contrib import admin

from menu.models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fields = ['name', 'parent']
    list_display = ['name', 'parent']
    ordering = ['parent']