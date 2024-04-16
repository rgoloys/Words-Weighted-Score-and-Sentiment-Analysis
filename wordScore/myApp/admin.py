# In admin.py
from django.contrib import admin
from .models import KeyWord, AcceptScore
from .models import AdminInput
from .models import FileKeywordCount, UploadedFile
from datetime import date, timedelta
from dateutil.relativedelta import relativedelta
from django.utils.translation import gettext_lazy as _
from django.contrib.admin import SimpleListFilter
from dateutil.parser import parse as parse_date
from django.utils.html import format_html
from django import forms
from django.urls import reverse
from bootstrap_daterangepicker import widgets, fields

class KeyWordAdmin(admin.ModelAdmin):
    list_display = ('keywords', 'score', 'admin_user', 'date_added', 'color_code')  # Include 'score' in the list display

class AcceptScoreAdmin(admin.ModelAdmin):
    list_display = ('score', 'admin_user', 'date_added')  # Specify fields to display in the list view

class AdminInputAdmin(admin.ModelAdmin):
    list_display = ('paragraph', 'color')  # Include 'score' in the list display


class DateRangeForm(forms.Form):
    start_date = forms.DateField(label=_('Start Date'), widget=forms.DateInput(attrs={'type': 'date'}))
    end_date = forms.DateField(label=_('End Date'), widget=forms.DateInput(attrs={'type': 'date'}))

class DateAddedRangeFilter(admin.SimpleListFilter):
    title = _('Date Added Range')
    parameter_name = 'date_added_range'

    def lookups(self, request, model_admin):
        return (
            ('today', _('Today')),
            ('this_week', _('This week')),
            ('this_month', _('This month')),
            ('custom', _('Custom date range')),
        )

    def queryset(self, request, queryset):
        if self.value() == 'today':
            return queryset.filter(date_added=date.today())
        elif self.value() == 'this_week':
            start_of_week = date.today() - timedelta(days=date.today().weekday())
            end_of_week = start_of_week + timedelta(days=6)
            return queryset.filter(date_added__range=[start_of_week, end_of_week])
        elif self.value() == 'this_month':
            start_of_month = date.today().replace(day=1)
            end_of_month = start_of_month + relativedelta(months=1, days=-1)
            return queryset.filter(date_added__range=[start_of_month, end_of_month])
        elif self.value() == 'custom':
            form = DateRangeForm(request.GET)
            if form.is_valid():
                start_date = form.cleaned_data['start_date']
                end_date = form.cleaned_data['end_date']
                return queryset.filter(date_added__range=[start_date, end_date])
        return queryset

class FileKeywordCountAdmin(admin.ModelAdmin):
    list_display = ('user_link','file', 'file_type', 'calculate_overall_total',  'date_added')
    readonly_fields = ('calculate_overall_total',)
    list_filter = (DateAddedRangeFilter, 'user', 'file_type')

    def user_link(self, obj):
        # Generate a link to filter files by user
        return format_html('<a href="{}?user={}">{}</a>',
                           reverse('admin:myApp_filekeywordcount_changelist'),
                           obj.user.id,
                           obj.user.username)
    user_link.admin_order_field = 'user__username'  # Allow sorting by username

admin.site.register(FileKeywordCount, FileKeywordCountAdmin)


@admin.register(UploadedFile)
class UploadedFileAdmin(admin.ModelAdmin):
    list_display = ('user', 'document', 'similarity_score', 'date_added')
    list_filter = (DateAddedRangeFilter, 'user')  # Added 'user' and 'document__file_type' to list_filter

    def user(self, obj):
        # Generate a link to filter files by user
        return format_html('<a href="{}?user={}">{}</a>',
                           reverse('admin:myApp_uploadedfile_changelist'),
                           obj.user.id,
                           obj.user.username)
    user.admin_order_field = 'user__username'  # Allow sorting by username


admin.site.register(KeyWord, KeyWordAdmin)
admin.site.register(AcceptScore, AcceptScoreAdmin)
admin.site.register(AdminInput, AdminInputAdmin)

