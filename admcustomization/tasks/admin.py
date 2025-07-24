from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'due_date', 'status', 'is_important')
    list_filter = ('status', 'is_important')
    search_fields = ('title', 'description')
    ordering = ('due_date', 'title')
    list_editable = ('is_important',)
    list_per_page = 10

    fieldsets = (
        ('Основна інформація', {
            'fields': ('title', 'description')
        }),
        ('Деталі', {
            'fields': ('due_date', 'status', 'is_important')
        }),
        ('Службова інформація', {
            'fields': ('created_at',),
            'classes': ('collapse',),
        }),
    )

    readonly_fields = ('created_at',)
