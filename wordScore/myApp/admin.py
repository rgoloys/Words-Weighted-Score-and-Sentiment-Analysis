# In admin.py
from django.contrib import admin
from .models import KeyWord, AcceptScore
from .models import AdminInput
from .models import FileKeywordCount, UploadedFile
from datetime import date, timedelta, datetime
from dateutil.relativedelta import relativedelta
from django.utils.translation import gettext_lazy as _
from django.contrib.admin import SimpleListFilter
from dateutil.parser import parse as parse_date
from django.utils.html import format_html
from django import forms
from django.urls import reverse
from django.contrib.auth.models import User
from rangefilter.filters import (
    DateRangeFilterBuilder,
    DateTimeRangeFilterBuilder,
    NumericRangeFilterBuilder,
    DateRangeQuickSelectListFilterBuilder,
)

#Filter by username
class UserFilter(admin.SimpleListFilter):
    title = _('User')
    parameter_name = 'user'

    def lookups(self, request, model_admin):
        users = User.objects.all()
        return [(user.id, user.username) for user in users]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(user_id=self.value())


#Filter by FILE_TYPE1
class FileKeywordType(admin.SimpleListFilter):
    title = _('File Type')
    parameter_name = 'file_type'

    def lookups(self, request, model_admin):
        # Get distinct file types from both models
        #uploaded_file_types = UploadedFile.objects.values_list('file_type', flat=True).distinct()
        keyword_file_types = FileKeywordCount.objects.values_list('file_type', flat=True).distinct()
        all_file_types = set(keyword_file_types)
        return [(file_type, file_type) for file_type in all_file_types]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(file_type=self.value())
        
#Filteration for KeywordScore Uploaded file
@admin.register(UploadedFile)
class UploadedFileAdmin(admin.ModelAdmin):
    list_display = ('user', 'document', 'similarity_score', 'date_added')
    list_filter = (UserFilter, ("date_added", DateRangeFilterBuilder(title=_("Filter by date"))),)
    UploadedFile._meta.verbose_name = "Sentiment Files Report"
    UploadedFile._meta.verbose_name_plural = "Sentiment Files Report"

#Filteration for FileKeywordCount Uploaded file
@admin.register(FileKeywordCount)
class FileKeywordCountAdmin(admin.ModelAdmin):
    list_display = ('user', 'file', 'file_type', 'calculate_overall_total', 'date_added')
    readonly_fields = ('calculate_overall_total',)
    list_filter = (UserFilter, FileKeywordType, ("date_added", DateRangeFilterBuilder(title=_("Filter by date"))))

    def calculate_overall_total(self, obj):
        overall_total = 0
        for data in obj.keyword_count.values():
            overall_total += data['total']
        return overall_total
    calculate_overall_total.short_description = 'Overall Score'
    
    FileKeywordCount._meta.verbose_name = "File Keywords Report"
    FileKeywordCount._meta.verbose_name_plural = "File Keywords Report"

#Funtion CRUD for Keyword, AcceptScore, AdminParagraph
class KeyWordAdmin(admin.ModelAdmin):
    list_display = ('keywords', 'score', 'admin_user', 'date_added', 'color_code')  # Include 'score' in the list display
    KeyWord._meta.verbose_name = "Add Keywords"
    KeyWord._meta.verbose_name_plural = "Add Keywords"

class AcceptScoreAdmin(admin.ModelAdmin):
    list_display = ('score', 'admin_user', 'date_added')  # Specify fields to display in the list view
    AcceptScore._meta.verbose_name = "Add Accepted Score"
    AcceptScore._meta.verbose_name_plural = "Add Accepted Score"

class AdminInputAdmin(admin.ModelAdmin):
    list_display = ('paragraph', 'color')  # Include 'score' in the list display
    AdminInput._meta.verbose_name = "Add Sentiment Paragraphs"
    AdminInput._meta.verbose_name_plural = "Add Sentiment Paragraphs"

admin.site.register(KeyWord, KeyWordAdmin)
admin.site.register(AcceptScore, AcceptScoreAdmin)
admin.site.register(AdminInput, AdminInputAdmin)
