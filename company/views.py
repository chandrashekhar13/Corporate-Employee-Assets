# company/views.py
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Device

class DeviceListView(ListView):
    model = Device
    template_name = 'company/device_list.html'
    context_object_name = 'devices'

class DeviceDetailView(DetailView):
    model = Device
    template_name = 'company/device_detail.html'
    context_object_name = 'device'
    
def employees_view(request):
    employees = Employee.objects.all()
    return render(request, 'employees.html', {'employees': employees})