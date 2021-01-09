from django.urls import path
from .views import ping, task
urlpatterns = [
    path('ping', ping.as_view()),
    path('', task.as_view()),
]
