from django.contrib import admin
from .models import Mobil, Service

@admin.register(Mobil)
class MobilAdmin(admin.ModelAdmin):
    list_display = ('merk', 'model', 'tahun', 'harga_dasar')

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('mobil', 'tanggal_service', 'biaya_service')
