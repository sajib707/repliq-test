from django.contrib import admin
from django.urls import path, include
from assets.views import company_list, employee_list, device_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', company_list), 
    path('employees/<int:company_id>/', employee_list),
    path('devices/<int:company_id>/', device_list),
]

