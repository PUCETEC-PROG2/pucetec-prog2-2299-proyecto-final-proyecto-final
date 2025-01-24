from django.contrib import admin

# Register your models here.
from .models import MusicProduct, ElectronicProduct, Product, Order, OrderItem, Client, OrderMusicItem, OrderElectronicItem

@admin.register(MusicProduct)
class MusicProductAdmin(admin.ModelAdmin):
    pass

@admin.register(ElectronicProduct)
class ElectronicProductAdmin(admin.ModelAdmin):
    pass

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    pass

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    pass

@admin.register(OrderMusicItem)
class OrderMusicItemAdmin(admin.ModelAdmin):
    pass

@admin.register(OrderElectronicItem)   
class OrderElectronicItemAdmin(admin.ModelAdmin):
    pass


