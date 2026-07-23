# ☕ VibeBrew-Cafe - Modern & Dinamik Django Kafe Web Uygulaması

![Vibe & Brew Cover](https://images.unsplash.com/photo-1501339847302-ac426a4a7cbb?auto=format&fit=crop&w=1200&q=80)

**VibeBrew-Cafe**, modern web mimarisi, zengin renk paleti ve yüksek performanslı Tailwind CSS arayüzü ile geliştirilmiş, tam kapsamlı bir **Django Kafe & Dijital Menü Web Uygulamasıdır**. 

Ziyaretçilere eşsiz bir dijital menü deneyimi, canlı sipariş sepeti, WhatsApp entegrasyonu, sürpriz kahve seçici ve interaktif açık/kapalı durumu gibi modern özellikler sunar.

---

## 🤖 Yapay Zeka Destekli Geliştirme (AI-Assisted Engineering)

Bu proje, modern geliştirme standartları doğrultusunda **Google DeepMind Antigravity AI** yapay zeka ikili kodlama (*pair-programming*) asistanı rehberliğinde mimarisi tasarlanmış, kodlanmış ve yayına hazırlanmıştır. Güncel yapay zeka araçlarının yazılım geliştirme süreçlerine entegrasyonunu sergileyen bir portföy çalışmasıdır.

---

## 🌟 Öne Çıkan Özellikler

- **📱 Dijital Menü & Kategori Filtreleme**: Sıcak İçecek, Soğuk İçecek, Tatlı ve Fırından ürünleri anında süzme ve canlı arama.
- **🛒 Canlı Sipariş Sepeti & WhatsApp Entegrasyonu**: Seçilen ürünlerin tutarını canlı hesaplayan sepet ve tek tıkla WhatsApp sipariş iletimi.
- **🏷️ İndirim Kuponu Sistemi**: `VIBE20` kodu ile anında %20 indirim uygulama imkanı.
- **🎁 Dijital Sadakat Kartı (Loyalty Pass)**: Her 6 siparişte 1 hediye kahve damgası sistemi.
- **🎲 Sürpriz Kahve Seçici ("Bana Kahve Öner!")**: Kararsız misafirler için eğlenceli algoritmik kahve önerici.
- **🔔 Canlı Neon Toast Bildirimleri**: Anlık eylemlerde kayarak açılan şık mikro bildirimler.
- **🟢 Canlı Çalışma Saatleri Rozeti**: Şu anki saate göre otomatik değişen "Şu An Açığız" / "Şu An Kapalıyız" rozeti.
- **🌙 Aydınlık / Karanlık Tema (Dark & Light Mode)**: Tek tıkla gece ve gündüz modları arasında geçiş.
- **📱 Masaya Özel QR Menü**: Masalarda okutulabilir dijital menü simülasyonu.
- **🎵 Spotify Playlist Barı**: Kafenin konsept müziğini sunan canlı equalizer efektli müzik barı.
- **💬 Sıkça Sorulan Sorular (SSS)**: İnteraktif akordiyon yanıt alanı.
- **🌐 RESTful JSON API Mimarisi**: `/api/lezzetler/` JSON veri uç noktası.
- **🔒 Güvenlik & Doğrulama**: Django ModelForm, CSRF koruması, Güvenli Form Handling, XSS ve SQL Injection önlemleri.

---

## 🛠️ Kullanılan Teknolojiler

- **Backend**: Python 3.14, Django 6.0 / 5.0 (MVC / MVT Mimarisi, RESTful JSON API)
- **Frontend**: HTML5, Vanilla JavaScript (ES6+), Tailwind CSS, FontAwesome 6
- **Database**: SQLite3 (Production için PostgreSQL uyumlu)
- **Static Assets & Deployment**: WhiteNoise, Gunicorn, Render.com Readiness
- **AI Pair Programming**: Google DeepMind Antigravity AI

---

## 🚀 Projeyi Yerelde Çalıştırma

Projeyi bilgisayarınızda klonlayıp çalıştırmak için aşağıdaki adımları izleyebilirsiniz:

```bash
# 1. Depoyu klonlayın
git clone https://github.com/KULLANICI_ADINIZ/VibeBrew-Cafe.git

# 2. Proje dizinine gidin
cd VibeBrew-Cafe

# 3. Gerekli kütüphaneleri yükleyin
pip install -r requirements.txt

# 4. Veritabanı migrasyonlarını uygulayın
python manage.py migrate

# 5. Geliştirici sunucusunu başlatın
python manage.py runserver 8000
```

Tarayıcınızdan `http://localhost:8000/` adresine girerek projeyi görüntüleyebilirsiniz.

---

## ☁️ Render.com Üzerinde Yayınlama (Deployment)

Proje **Render.com** veya **Vercel/Railway** gibi bulut platformlarına tek tıkla dağıtılmaya uygun `Procfile`, `requirements.txt` ve `WhiteNoise` static dosyaları ile yapılandırılmıştır.

---

## 📄 Lisans

Bu proje MIT Lisansı altında açık kaynaklı olarak paylaşılmıştır.
