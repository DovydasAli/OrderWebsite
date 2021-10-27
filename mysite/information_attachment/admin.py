from django.contrib import admin
from .models import Product, OrderProduct, Order, ImageOrderProduct, ImageOrder

class ProductAdmin(admin.ModelAdmin):
    list_display = ('number', 'status', 'link')
    list_editable = ('number', 'status')
    list_display_links = ('link',)
    search_fields = ('number',)

class OrderProductAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'ordered')
    list_editable = ('product',)
    search_fields = ('order__number',)

class OrderAdmin(admin.ModelAdmin):
    list_filter = ('status', 'date_created')
    list_display = ('number', 'status', 'date_created', 'ordered', 'display_products', 'link')
    list_editable = ('status', 'number')
    list_display_links = ('link',)
    search_fields = ('number',)
    readonly_fields = ['date_created']

    fieldsets = (
        (None, {
            'fields': ('number', 'ordered')
        }),
        ('Availability', {
            'fields': ('status', 'date_created')
        }),
    )

class ImageOrderProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'order_product', 'image')

admin.site.register(Product, ProductAdmin)
admin.site.register(OrderProduct, OrderProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(ImageOrderProduct, ImageOrderProductAdmin)
admin.site.register(ImageOrder)
