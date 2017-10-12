from django.contrib import admin
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    readonly_fields = ('timestamp_created',)
    list_display = ('real_name', 'username', 'email', 'timestamp_created')
    list_filter = ['timestamp_created']
    search_fields = ['real_name', 'username', 'email']

    fields = [
        'real_name', 'username', 'email', 'timestamp_created'
    ]
