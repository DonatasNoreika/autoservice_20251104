from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Service, Car, Order, OrderLine, OrderComment, CustomUser

class OrderLineInLine(admin.TabularInline):
    model = OrderLine
    extra = 0
    fields = ['service', 'quantity', 'line_sum']
    readonly_fields = ['line_sum']


class OrderCommentInLine(admin.TabularInline):
    model = OrderComment
    extra = 0

class OrderAdmin(admin.ModelAdmin):
    list_display = ['car', 'date', 'total', 'status', 'client', 'deadline', 'is_overdue']
    inlines = [OrderLineInLine, OrderCommentInLine]
    readonly_fields = ['date', 'total']

    fieldsets = [
        ('General', {'fields': ('car', 'date', 'total', 'status', 'client', 'deadline')}),
    ]

class CarAdmin(admin.ModelAdmin):
    list_display = ['make', 'model', 'license_plate', 'vin_code', 'client_name']
    list_filter = ['client_name', 'make', 'model']
    search_fields = ['license_plate', 'vin_code']

class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']


class OrderLineAdmin(admin.ModelAdmin):
    list_display = ['order', 'service', 'quantity', 'line_sum']

class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('photo',)}),
    )

admin.site.register(Service, ServiceAdmin)
admin.site.register(Car, CarAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderLine, OrderLineAdmin)
admin.site.register(CustomUser, CustomUserAdmin)
