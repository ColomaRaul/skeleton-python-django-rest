from django.urls import path

from api.infrastructure.ping_view import PingView
from api.infrastructure.test_view import TestView

app_name = 'api'

urlpatterns = [
    path('ping', PingView.as_view()),
    path('testing', TestView.as_view()),
]
