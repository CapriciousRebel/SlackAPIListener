from django.urls import path

from . import views

# set namespace polls
app_name = 'FileHandler'

urlpatterns = [
    path('drive_backup', views.drive_backup, name='drive_backup'),
]
