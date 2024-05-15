from django.urls import path
from .views import *

urlpatterns = [
    path('view_logs/', LogListView.as_view()),
    path('view_logs/filter_response/<str:filter_response>', LogListResponseView.as_view()),
]