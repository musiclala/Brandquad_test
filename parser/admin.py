from django.contrib import admin
from .models import Log


@admin.register(Log)
class LogAdmin(admin.ModelAdmin):
    list_display = (
        'remote_ip', 'time', 'remote_user', 'request_method', 'request_url', 'response', 'bytes_response', 'referrer',
        'agent', 'created_at', 'updated_at')
    search_fields = ('remote_ip', 'request_method', 'request_url', 'response')
    list_filter = ('response', 'request_method')
