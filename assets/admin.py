from django.contrib import admin
from .models import Company, Employee, Device

class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name']

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['name', 'company']

class DeviceAdmin(admin.ModelAdmin):
    list_display = ['name', 'company', 'condition', 'assigned_to', 'checkout_date', 'return_date']

admin.site.register(Company, CompanyAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Device, DeviceAdmin)
