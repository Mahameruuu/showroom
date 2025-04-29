from django.shortcuts import render, redirect, get_object_or_404
from .models import Mobil, Service
from django.urls import reverse
from django.utils import timezone
from .forms import MobilForm 

def daftar_mobil(request):
    mobils = Mobil.objects.all()
    return render(request, 'showroom/daftar_mobil.html', {'mobils': mobils})

def tambah_mobil(request):
    if request.method == 'POST':
        merk = request.POST['merk']
        model = request.POST['model']
        tahun = request.POST['tahun']
        harga_dasar = request.POST['harga_dasar']
        pinjaman = request.POST.get('pinjaman') or None
        suku_bunga = request.POST.get('suku_bunga') or None

        mobil = Mobil(
            merk=merk,
            model=model,
            tahun=tahun,
            harga_dasar=harga_dasar,
            pinjaman=pinjaman,
            suku_bunga=suku_bunga
        )
        mobil.save()
        return redirect('daftar_mobil')
    return render(request, 'showroom/tambah_mobil.html')

def edit_mobil(request, id):
    mobil = get_object_or_404(Mobil, id=id)
    if request.method == 'POST':
        form = MobilForm(request.POST, instance=mobil)
        if form.is_valid():
            form.save()
            return redirect('daftar_mobil')
    else:
        form = MobilForm(instance=mobil)
    return render(request, 'showroom/edit_mobil.html', {'form': form, 'mobil': mobil})

def detail_mobil(request, mobil_id):
    mobil = get_object_or_404(Mobil, id=mobil_id)
    return render(request, 'showroom/detail_mobil.html', {'mobil': mobil})

def tambah_service(request, mobil_id):
    mobil = get_object_or_404(Mobil, id=mobil_id)
    if request.method == 'POST':
        tanggal_service = request.POST['tanggal_service']
        deskripsi_service = request.POST['deskripsi_service']
        biaya_service = request.POST['biaya_service']

        service = Service(
            mobil=mobil,
            tanggal_service=tanggal_service,
            deskripsi_service=deskripsi_service,
            biaya_service=biaya_service
        )
        service.save()
        return redirect('detail_mobil', mobil_id=mobil.id)
    return render(request, 'showroom/tambah_service.html', {'mobil': mobil})

def hapus_mobil(request, mobil_id):
    mobil = get_object_or_404(Mobil, id=mobil_id)
    mobil.delete()
    return redirect('daftar_mobil')
