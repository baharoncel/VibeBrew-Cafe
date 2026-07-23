from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from .models import Lezzet, Rezervasyon
from .forms import RezervasyonForm

VAR_VARSAYILAN_LEZZETLER = [
    {
        "isim": "Gökkuşağı Latte",
        "kategori": "Sıcak İçecek",
        "aciklama": "Özel kadife süt köpüğü, vanilya aroması ve canlı renk sunumuyla gününüzü aydınlatır.",
        "fiyat": "140 TL",
        "renk": "from-pink-500 to-rose-500",
        "ikon": "fa-mug-hot",
        "resim": "https://images.unsplash.com/photo-1541167760496-1628856ab772?auto=format&fit=crop&w=600&q=80",
        "rozet": "⭐ Şefin Tavsiyesi",
        "diyet": "🥛 Badem Sütü • 160 kcal",
        "sure": "⏱️ Hazırlanma: 4-6 Dk",
        "sira": 1
    },
    {
        "isim": "Karamel Macchiato",
        "kategori": "Sıcak İçecek",
        "aciklama": "Yoğun espresso, buharla köpürtülmüş taze süt ve ev yapımı tereyağlı karamel sosu.",
        "fiyat": "150 TL",
        "renk": "from-amber-600 to-yellow-500",
        "ikon": "fa-mug-saucer",
        "resim": "https://images.unsplash.com/photo-1485808191679-5f86510681a2?auto=format&fit=crop&w=600&q=80",
        "rozet": "☕ Günün Kahvesi",
        "diyet": "🌾 Glutensiz • 210 kcal",
        "sure": "⏱️ Hazırlanma: 3-5 Dk",
        "sira": 2
    },
    {
        "isim": "Tropikal Berry Smoothie",
        "kategori": "Soğuk İçecek",
        "aciklama": "Çilek, yaban mersini, badem sütü ve ferahlatıcı nane yapraklarının eşsiz karışımı.",
        "fiyat": "160 TL",
        "renk": "from-emerald-400 to-cyan-500",
        "ikon": "fa-glass-water",
        "resim": "https://images.unsplash.com/photo-1553530666-ba11a7da3888?auto=format&fit=crop&w=600&q=80",
        "rozet": "🧊 Ferahlatıcı",
        "diyet": "🌱 Vegan • 140 kcal",
        "sure": "⏱️ Hazırlanma: 5 Dk",
        "sira": 3
    },
    {
        "isim": "Iced Hibiscus Tea",
        "kategori": "Soğuk İçecek",
        "aciklama": "Demlenmiş hibiskus çiçeği, taze nar taneleri, limon dilimleri ve kırık buz.",
        "fiyat": "130 TL",
        "renk": "from-rose-500 to-red-600",
        "ikon": "fa-wine-glass",
        "resim": "https://images.unsplash.com/photo-1513558161293-cdaf765ed2fd?auto=format&fit=crop&w=600&q=80",
        "rozet": "",
        "diyet": "🌱 Vegan • 90 kcal",
        "sure": "⏱️ Hazırlanma: 3 Dk",
        "sira": 4
    },
    {
        "isim": "Orman Meyveli Cheesecake",
        "kategori": "Tatlı & Pasta",
        "aciklama": "Taze böğürtlen, ahududu ve çıtır bisküvi tabanıyla hazırlanan imza tatlımız.",
        "fiyat": "180 TL",
        "renk": "from-purple-500 to-indigo-500",
        "ikon": "fa-cake-candles",
        "resim": "https://images.unsplash.com/photo-1533134242443-d4fd215305ad?auto=format&fit=crop&w=600&q=80",
        "rozet": "🍰 Özel Tarif",
        "diyet": "🍰 Günlük Taze • 320 kcal",
        "sure": "⏱️ Servis Süresi: 2 Dk",
        "sira": 5
    },
    {
        "isim": "San Sebastian Cheesecake",
        "kategori": "Tatlı & Pasta",
        "aciklama": "İçi akışkan, üzeri karamelize edilmiş İspanyol lezzeti. Yanında eritilmiş Belçika çikolatası ile.",
        "fiyat": "200 TL",
        "renk": "from-amber-700 to-orange-600",
        "ikon": "fa-cheese",
        "resim": "https://images.unsplash.com/photo-1621303837174-89787a7d4729?auto=format&fit=crop&w=600&q=80",
        "rozet": "🔥 En Çok Satan",
        "diyet": "🌾 Glutensiz • 380 kcal",
        "sure": "⏱️ Servis Süresi: 3 Dk",
        "sira": 6
    },
    {
        "isim": "Çıtır Tereyağlı Kruvasan",
        "kategori": "Fırından",
        "aciklama": "Her sabah fırından yeni çıkan, Belçika çikolatası dolgulu çıtır lezzet.",
        "fiyat": "110 TL",
        "renk": "from-amber-500 to-orange-500",
        "ikon": "fa-bread-slice",
        "resim": "https://images.unsplash.com/photo-1555507036-ab1f4038808a?auto=format&fit=crop&w=600&q=80",
        "rozet": "🥐 Taze Çıktı",
        "diyet": "🥐 Fransız Tereyağı • 260 kcal",
        "sure": "⏱️ Fırından Taze: 8 Dk",
        "sira": 7
    },
    {
        "isim": "Avokado & Poşe Yumurta Toast",
        "kategori": "Fırından",
        "aciklama": "Ekşi maya ekmek üzerinde ezilmiş avokado, çeri domates ve tam kıvamında poşe yumurta.",
        "fiyat": "220 TL",
        "renk": "from-green-600 to-emerald-500",
        "ikon": "fa-egg",
        "resim": "https://images.unsplash.com/photo-1525351484163-7529414344d8?auto=format&fit=crop&w=600&q=80",
        "rozet": "🥑 Fit Seçim",
        "diyet": "🌱 Protein Deposu • 290 kcal",
        "sure": "⏱️ Hazırlanma: 8-10 Dk",
        "sira": 8
    }
]

def cafe_tanitim(request):
    if Lezzet.objects.count() == 0 or not Lezzet.objects.filter(sure__contains="Dk").exists():
        Lezzet.objects.all().delete()
        for item in VAR_VARSAYILAN_LEZZETLER:
            Lezzet.objects.create(**item)

    lezzetler = Lezzet.objects.filter(aktif=True)
    form = RezervasyonForm()

    if request.method == "POST":
        form = RezervasyonForm(request.POST)
        if form.is_valid():
            form.save()
            isim = form.cleaned_data.get('isim')
            messages.success(request, f"Harika {isim}! Mesajınız bize ulaştı, en kısa sürede sizinle iletişime geçeceğiz 🌈")
            return redirect("cafe_tanitim")
        else:
            messages.error(request, "Lütfen formdaki tüm alanları eksiksiz ve doğru doldurunuz.")

    context = {
        "lezzetler": lezzetler,
        "form": form
    }
    return render(request, "index.Html", context)


# 🌐 RESTful JSON API Ucu
def api_lezzetler(request):
    lezzetler = Lezzet.objects.filter(aktif=True)
    data = []
    for item in lezzetler:
        data.append({
            "id": item.id,
            "isim": item.isim,
            "kategori": item.kategori,
            "aciklama": item.aciklama,
            "fiyat": item.fiyat,
            "rozet": item.rozet,
            "diyet": item.diyet,
            "sure": item.sure,
            "resim": item.resim
        })
    return JsonResponse({
        "success": True,
        "count": len(data),
        "data": data
    }, safe=False, json_dumps_params={'ensure_ascii': False})