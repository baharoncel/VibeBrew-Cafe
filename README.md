# ☕ VibeBrew-Cafe - Modern & Dinamik Django Kafe Web Uygulaması

[![Live Demo](https://img.shields.io/badge/Live_Demo-https%3A%2F%2Fvibebrew--cafe.onrender.com-brightgreen?style=for-the-badge&logo=render)](https://vibebrew-cafe.onrender.com)
[![Django](https://img.shields.io/badge/Django-5.0%2B-092E20?style=for-the-badge&logo=django)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.12%2B-3776AB?style=for-the-badge&logo=python)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)](LICENSE)

![Vibe & Brew Cover](https://images.unsplash.com/photo-1501339847302-ac426a4a7cbb?auto=format&fit=crop&w=1200&q=80)

> 🔗 **Canlı Demo Adresi:** [https://vibebrew-cafe.onrender.com](https://vibebrew-cafe.onrender.com)

**VibeBrew-Cafe**, modern web mimarisi, zengin renk paleti ve yüksek performanslı Tailwind CSS arayüzü ile geliştirilmiş, tam kapsamlı bir **Django Kafe & Dijital Menü Web Uygulamasıdır**. 

---

## 🎓 Geliştirici Notu (Backend Student Portfolio Project)

Bu proje, bir **Backend Developer Öğrencisi** olarak endüstri standartlarında Django MVT mimarisi, veritabanı modellemesi (ORM), sunucu taraflı form güvenliği (ModelForm), RESTful JSON API tasarımı, ortam değişkenleri güvenliği (`.env` & `python-dotenv`) ve bulut ortamında yayına alma (Deployment) pratiklerini sergilemek amacıyla geliştirilmiştir.

---

## 🤖 Yapay Zeka Destekli Geliştirme (AI-Assisted Engineering)

Bu proje, modern geliştirme standartları doğrultusunda **Google DeepMind Antigravity AI** yapay zeka ikili kodlama (*pair-programming*) asistanı rehberliğinde mimarisi tasarlanmış, kodlanmış ve yayına hazırlanmıştır. Güncel yapay zeka araçlarının yazılım geliştirme süreçlerine entegrasyonunu sergileyen bir portföy çalışmasıdır.

---

## 🏛️ Mimari Yapı & Sistem Tasarımı (Django MVT)

Proje, Django'nun **Model-View-Template (MVT)** mimarisi üzerine inşa edilmiştir:

```
VibeBrew-Cafe/
├── app/                        # Ana Django Uygulaması
│   ├── models.py               # Ürün, Kategori & İletişim ORM Modelleri
│   ├── views.py                # Sayfa Mantığı & REST API Endpoints
│   ├── forms.py                # ModelForm ile Sunucu Taraflı Doğrulama
│   ├── urls.py                 # Uygulama Yönlendirmeleri
│   └── templates/              # HTML5 & Tailwind UI Şablonları
├── coffe/                      # Proje Yapılandırma Dizinı
│   ├── settings.py             # Güvenlik, Static Files & App Ayarları
│   └── urls.py                 # Ana URL Routing
├── .env.example                # Güvenli Ortam Değişkenleri Şablonu
├── .gitignore                  # Hassas Veri & Bağımlılık Koruma Kuralı
├── Procfile                    # Render.com Gunicorn Dağıtım Komutu
└── requirements.txt            # Proje Bağımlılıkları
```

---

## 🌐 RESTful API Endpoints

| Metot | Uç Nokta | Açıklama |
|---|---|---|
| `GET` | `/` | Canlı Dijital Menü, Sepet, Sadakat Kartı ve İletişim Arayüzü |
| `GET` | `/api/lezzetler/` | Tüm ürün ve kategorileri JSON formatında sunan REST API |
| `POST` | `/` | İletişim formu verilerini sunucu taraflı doğrulama (ModelForm) ile kaydetme |

---

## 🌟 Öne Çıkan Özellikler

- **📱 Dijital Menü & Canlı Filtreleme**: Sıcak İçecek, Soğuk İçecek, Tatlı ve Fırından ürünlerini anında süzme ve canlı arama.
- **🛒 Canlı Sipariş Sepeti & WhatsApp Entegrasyonu**: Seçilen ürünlerin tutarını canlı hesaplayan sepet ve tek tıkla WhatsApp sipariş iletimi.
- **🏷️ İndirim Kuponu Sistemi**: `VIBE20` kodu ile anında %20 indirim uygulama imkanı.
- **🎁 Dijital Sadakat Kartı (Loyalty Pass)**: Her 6 siparişte 1 hediye kahve damgası sistemi.
- **🎲 Sürpriz Kahve Seçici ("Bana Kahve Öner!")**: Kararsız misafirler için eğlenceli algoritmik kahve önerici.
- **🔔 Canlı Neon Toast Bildirimleri**: Anlık eylemlerde kayarak açılan şık mikro bildirimler.
- **🟢 Canlı Çalışma Saatleri Rozeti**: Şu anki saate göre otomatik değişen "Şu An Açığız" / "Şu An Kapalıyız" rozeti.
- **🌙 Aydınlık / Karanlık Tema (Dark & Light Mode)**: Tek tıkla gece ve gündüz modları arasında geçiş.
- **📱 Masaya Özel QR Menü**: Masalarda okutulabilir dijital menü simülasyonu.
- **🎵 Spotify Playlist Barı**: Kafenin konsept müziğini sunan canlı equalizer efektli müzik barı.
- **🔒 Güvenlik & Doğrulama**: Django ModelForm, CSRF koruması, `.env` gizliliği, XSS ve SQL Injection önlemleri.

---

## 🛠️ Kullanılan Teknolojiler

- **Backend**: Python 3.12+, Django 5.0+ (MVT Mimarisi, ORM, REST API)
- **Güvenlik**: `python-dotenv`, CSRF Token, Clean Form Validation
- **Frontend**: HTML5, Vanilla JavaScript (ES6+), Tailwind CSS, FontAwesome 6
- **Database**: SQLite3 (Production için PostgreSQL uyumlu)
- **Static Assets & Deployment**: WhiteNoise, Gunicorn, Render.com

---

## 🚀 Projeyi Yerelde Çalıştırma

Projeyi bilgisayarınızda klonlayıp çalıştırmak için aşağıdaki adımları izleyebilirsiniz:

```bash
# 1. Depoyu klonlayın
git clone https://github.com/baharoncel/VibeBrew-Cafe.git

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

Proje **Render.com** üzerinde canlıda çalışmaktadır. Repoya yapılan her `git push` işlemi **Auto-Deploy** mekanizması sayesinde canlı ortama otomatik olarak yansıtılmaktadır.

---

## 📄 Lisans

Bu proje MIT Lisansı altında açık kaynaklı olarak paylaşılmıştır.
