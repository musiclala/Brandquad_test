from rest_framework import generics
from .models import Log
from .serializers import LogListSerializer
from .service import PaginationLog


class LogListView(generics.ListAPIView):
    """Вывести список всех логов"""
    queryset = Log.objects.all()
    serializer_class = LogListSerializer
    pagination_class = PaginationLog


class LogListResponseView(generics.ListAPIView):
    """Фильтрация по статусу ответа, например, по идее это же и поиск?"""
    serializer_class = LogListSerializer
    pagination_class = PaginationLog

    def get_queryset(self, **kwargs):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        response = self.kwargs['filter_response']
        print(response)
        return Log.objects.filter(response=response)

