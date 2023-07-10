# company/urls.py
from django.urls import path
from . import views

app_name = 'company'

urlpatterns = [
    path('devices/', views.DeviceListView.as_view(), name='device_list'),
    path('devices/<int:pk>/', views.DeviceDetailView.as_view(), name='device_detail'),
    path('employees/', employees_view, name='employees'),
    # Add more URLs as needed
]
