from django.contrib import admin
from .models import Offer, OfferDetail

@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at', 'user')
    search_fields = ('title', 'description', 'user__username')
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('-created_at',)
    
@admin.register(OfferDetail)
class OfferDetailAdmin(admin.ModelAdmin):
    list_display = ('title', 'offer', 'offer_type', 'price', 'delivery_time_in_days', 'revisions')
    list_filter = ('offer_type', 'offer__user')
    search_fields = ('title', 'offer__title', 'offer__user__username')
    ordering = ('offer', 'offer_type')
