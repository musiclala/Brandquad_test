from django.core.management import call_command
from django.test import TestCase
from rest_framework.test import RequestsClient
# Using the standard RequestFactory API to create a form POST request
client = RequestsClient()


class CommandsTestCase(TestCase):
    def test_command_success(self):
        """Тест на успешность команды"""

        args = [r'D:\Pycharm proj\Brandquad_test\parser\management\commands\nginx_json_logs.txt']
        opts = {}
        a = call_command('Parser_logs', *args, **opts)
        self.assertEquals(a, "success")

    def test_command_error(self):
        """Тест на несуществующий файл команды"""

        args = [r'D:\Pycharm proj\Brandquad_test\parser\management\commands\nginx_json_logs.tx']
        opts = {}
        a = call_command('Parser_logs', *args, **opts)
        self.assertEquals(a, "error")

    def test_view_logs_success(self):
        """Тест на view_logs 200 - api"""

        request = client.get('http://localhost:8000/api/view_logs/')
        self.assertEquals(request.status_code, 200)

    def test_view_logs_error(self):
        """Тест на view_logs 404 - api"""

        request = client.get('http://localhost:8000/api/view_log/')
        self.assertEquals(request.status_code, 404)

    def test_filter_response_success(self):
        """Тест на filter_response 200 - api"""

        request = client.get('http://localhost:8000/api/view_logs/filter_response/200')
        self.assertEquals(request.status_code, 200)

    def test_filter_response_error(self):
        """Тест на filter_response 500 - api"""

        request = client.get('http://localhost:8000/api/view_logs/filter_response/qwerty')
        self.assertEquals(request.status_code, 500)
