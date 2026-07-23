from django.db import models

class Lezzet(models.Model):
    KATEGORI_SECENEKLERI = [
        ('Sıcak İçecek', 'Sıcak İçecek'),
        ('Soğuk İçecek', 'Soğuk İçecek'),
        ('Tatlı & Pasta', 'Tatlı & Pasta'),
        ('Fırından', 'Fırından'),
    ]

    isim = models.CharField(max_length=100, verbose_name="Lezzet Adı")
    kategori = models.CharField(max_length=50, choices=KATEGORI_SECENEKLERI, verbose_name="Kategori")
    aciklama = models.TextField(verbose_name="Açıklama")
    fiyat = models.CharField(max_length=20, verbose_name="Fiyat (Örn: 150 TL)")
    renk = models.CharField(max_length=100, default="from-pink-500 to-rose-500", verbose_name="Renk Geçişi CSS")
    ikon = models.CharField(max_length=50, default="fa-mug-hot", verbose_name="FontAwesome İkon")
    resim = models.URLField(max_length=500, verbose_name="Resim URL")
    rozet = models.CharField(max_length=50, blank=True, default="", verbose_name="Özel Rozet")
    diyet = models.CharField(max_length=100, blank=True, default="", verbose_name="Diyet & Besin Etiketleri")
    sure = models.CharField(max_length=50, blank=True, default="⏱️ 4-6 Dk", verbose_name="Hazırlanma Süresi")
    aktif = models.BooleanField(default=True, verbose_name="Sitede Gösterilsin mi?")
    sira = models.IntegerField(default=0, verbose_name="Görüntülenme Sırası")

    class Meta:
        verbose_name = "Lezzet"
        verbose_name_plural = "Lezzetler"
        ordering = ['sira', 'id']

    def __str__(self):
        return f"{self.isim} ({self.kategori})"


class Rezervasyon(models.Model):
    isim = models.CharField(max_length=100, verbose_name="Ad Soyad")
    telefon = models.CharField(max_length=20, verbose_name="Telefon Numarası")
    mesaj = models.TextField(verbose_name="Mesaj veya Rezervasyon Detayı")
    tarih = models.DateTimeField(auto_now_add=True, verbose_name="Gönderilme Tarihi")
    okundu = models.BooleanField(default=False, verbose_name="İncelendi / Okundu")

    class Meta:
        verbose_name = "Rezervasyon & Mesaj"
        verbose_name_plural = "Rezervasyonlar & Mesajlar"
        ordering = ['-tarih']

    def __str__(self):
        return f"{self.isim} - {self.telefon} ({self.tarih.strftime('%d.%m.%Y %H:%M')})"
