from django.contrib import admin
from .models import NetworkNode, Supplier, Product
from django.utils.html import format_html

admin.site.register(Supplier)
admin.site.register(Product)

@admin.register(NetworkNode)
class NetworkNodeAdmin(admin.ModelAdmin):
    list_display = ('name', 'level', 'supplier_link', 'city', 'created_at', 'debt_to_supplier')
    list_filter = ('city', 'level')
    search_fields = ('name', 'city')
    actions = ['clean_debt']

    fieldsets = (
        (None, {
            'fields': ('name', 'level', 'supplier', 'parent', 'email', 'country', 'city', 'street', 'house_number', 'products')
        }),
        ('Финансы', {
            'fields': ('debt_to_supplier',)
        }),
    )

    def supplier_link(self, obj):
        if obj.supplier:
            url = f"/admin/network/supplier/{obj.supplier.id}/change/"
            return format_html("{}", url, obj.supplier.name)
        return "-"
    supplier_link.short_description = "Поставщик"

    def clean_debt(self, request, queryset):
        for obj in queryset:
            obj.clean_debt()
        self.message_user(request, f"Задолженность очищена у {queryset.count()} объектов.")
    clean_debt.short_description = "Очистить задолженность перед поставщиком"
