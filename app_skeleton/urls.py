from django.urls import path
from . import views

app_name = 'app_skeleton'  # Optional, if you want to namespace your app's URLs

urlpatterns = [
    path('app_skeleton/', views.my_view, name='my_view'),
    ...
]
