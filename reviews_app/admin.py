from django.contrib import admin
from .models import Review

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'business_user', 'reviewer', 'rating', 'created_at', 'updated_at')
    list_filter = ('rating', 'created_at', 'updated_at', 'business_user')
    search_fields = ('business_user__username', 'reviewer__username', 'description')
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('-created_at',)
