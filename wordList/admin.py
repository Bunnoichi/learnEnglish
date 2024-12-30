from django.contrib import admin
from .models import Card

# admin.site.register(Card)

@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
   readonly_fields = ['id', 'word', 'meaning', 'note', 'created_at']