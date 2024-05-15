from rest_framework.pagination import PageNumberPagination


class PaginationLog(PageNumberPagination):
    page_size = 10
    max_page_size = 1000