from django.db import models

class Mobil(models.Model):
    merk = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    tahun = models.IntegerField()
    harga_dasar = models.DecimalField(max_digits=12, decimal_places=2)
    pinjaman = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    suku_bunga = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"{self.merk} {self.model} ({self.tahun})"

    def cicilan_bulanan(self):
        if self.pinjaman and self.suku_bunga:
            bunga_per_bulan = self.suku_bunga / 12 / 100
            return (self.pinjaman * (1 + bunga_per_bulan)) / 12
        return 0

    def hpp(self):
        total_service = sum(service.biaya_service for service in self.services.all())
        if self.pinjaman and self.suku_bunga:
            total_pinjaman = self.pinjaman + (self.pinjaman * self.suku_bunga / 100)
            return (self.harga_dasar / total_pinjaman) + total_service
        return self.harga_dasar + total_service

class Service(models.Model):
    mobil = models.ForeignKey(Mobil, related_name='services', on_delete=models.CASCADE)
    tanggal_service = models.DateField()
    deskripsi_service = models.TextField()
    biaya_service = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f"Service {self.mobil.merk} {self.mobil.model} pada {self.tanggal_service}"
