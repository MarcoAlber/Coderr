from django.contrib import admin
from .models import UserProfile

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'type', 'location', 'tel', 'created_at')
    list_filter = ('type', 'created_at')
    search_fields = ('user__username', 'user__email', 'location', 'tel')
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)
