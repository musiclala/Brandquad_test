from django.db import models


class Log(models.Model):
    """Модель для логов"""
    remote_ip = models.CharField(verbose_name='IP адрес', max_length=50)
    time = models.DateTimeField(verbose_name='Дата записи лога')
    remote_user = models.CharField(verbose_name='Пользователь', max_length=50)
    request_method = models.CharField(verbose_name='Метод запроса', max_length=10)
    request_url = models.CharField(verbose_name='URL запроса', max_length=10)
    response = models.IntegerField(verbose_name='Статус запроса')
    bytes_response = models.IntegerField(verbose_name='Размер запроса')
    referrer = models.CharField(verbose_name='URL запроса', max_length=50)
    agent = models.CharField(verbose_name='URL запроса', max_length=200)

    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Дата изменения', auto_now=True)

    def __str__(self):
        return self.remote_ip

    class Meta:
        verbose_name = 'Лог'
        verbose_name_plural = 'Логи'
        ordering = ['-time']
