from django.contrib import admin
from .models import Meal


@admin.register(Meal)
class MealAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'category',
        'day_linked',
        'price',
        'enabled',
        'timestamp_created'
    ]
    list_filter = ['timestamp_created']
    search_fields = [
        'title',
        'category',
        'day_linked'
    ]
