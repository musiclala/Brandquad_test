import datetime

from django.core.management.base import BaseCommand
from parser.models import Log
import json
import warnings


warnings.filterwarnings('ignore')


class Command(BaseCommand):

    def add_arguments(self, parser):
        """Добавляем аргумент к функции в виде пути до файла."""
        parser.add_argument('path_to_file', nargs='+', type=str,
                            help='path_to_file')

    def handle(self, *args, **options):
        """Парсим файл и записываем в бд"""
        try:
            # Получаем введеный в аргументах путь
            path_to_file = options['path_to_file'][0]
            # Считываем построчно
            with open(path_to_file, 'r') as f:
                answer = f.read().splitlines()
            result = []
            updated_values = {}
            # Пробегаемся по всем строкам, парсим их и добавляет как объект Log, для bulk_create
            for item in answer:
                a = json.loads(item)
                updated_values['remote_ip'] = a['remote_ip']
                updated_values['time'] = datetime.datetime.strptime(a['time'].partition(' +')[0], '%d/%b/%Y:%H:%M:%S')
                updated_values['remote_user'] = a['remote_user']
                updated_values['request_method'] = a['request'].partition('/')[0].strip()
                updated_values['request_url'] = a['request'].partition('/')[2]
                updated_values['response'] = a['response']
                updated_values['bytes_response'] = a['bytes']
                updated_values['referrer'] = a['referrer']
                updated_values['agent'] = a['agent']
                result.append(Log(**updated_values))
            Log.objects.bulk_create(result)
            return 'success'
        except Exception as ex:
            return 'error'

