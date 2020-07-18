from django.urls import path

from . import views

# set namespace polls
app_name = 'Rerouter'

urlpatterns = [
    path('', views.rerouter, name='rerouter'),
]
