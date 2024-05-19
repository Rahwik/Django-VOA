from django.urls import path
from .views import home, process_command

urlpatterns = [
    path('', home, name='home'),
    path('process_command/', process_command, name='process_command'),
]
