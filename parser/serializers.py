from rest_framework import serializers
from .models import Log


class LogListSerializer(serializers.ModelSerializer):
    """Вывод списка логов"""

    class Meta:
        model = Log
        fields = (
            'remote_ip', 'time', 'remote_user', 'request_method', 'request_url', 'response', 'bytes_response',
            'referrer', 'agent', 'created_at', 'updated_at')
