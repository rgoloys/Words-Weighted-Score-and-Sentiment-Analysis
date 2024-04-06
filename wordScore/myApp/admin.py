# In admin.py
from django.contrib import admin
from .models import KeyWord, AcceptScore
from .models import AdminInput


class KeyWordAdmin(admin.ModelAdmin):
    list_display = ('keywords', 'score', 'admin_user', 'date_added', 'color_code')  # Include 'score' in the list display

class AcceptScoreAdmin(admin.ModelAdmin):
    list_display = ('score', 'admin_user', 'date_added')  # Specify fields to display in the list view

class AdminInputAdmin(admin.ModelAdmin):
    list_display = ('paragraph', 'color')  # Include 'score' in the list display


admin.site.register(KeyWord, KeyWordAdmin)
admin.site.register(AcceptScore, AcceptScoreAdmin)
admin.site.register(AdminInput, AdminInputAdmin)
