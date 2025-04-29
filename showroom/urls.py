from django.urls import path
from . import views

urlpatterns = [
    path('', views.daftar_mobil, name='daftar_mobil'),
    path('tambah/', views.tambah_mobil, name='tambah_mobil'),
    path('mobil/<int:mobil_id>/', views.detail_mobil, name='detail_mobil'),
    path('showroom/edit/<int:id>/', views.edit_mobil, name='edit_mobil'),
    path('mobil/<int:mobil_id>/tambah_service/', views.tambah_service, name='tambah_service'),
    path('mobil/<int:mobil_id>/hapus/', views.hapus_mobil, name='hapus_mobil'),
]
