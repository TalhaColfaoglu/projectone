# Talha Colfaoğlu - Kişisel Website

Modern ve profesyonel bir kişisel website/CV sitesi. Django backend'i ile geliştirilmiş, responsive tasarım ve modern UI/UX prensipleri kullanılarak oluşturulmuştur.

## 🚀 Özellikler

- **Modern Tasarım**: Bootstrap 5 ve modern CSS ile responsive tasarım
- **Animasyonlar**: AOS (Animate On Scroll) ile smooth animasyonlar
- **Admin Paneli**: Django admin ile kolay içerik yönetimi
- **İletişim Formu**: Fonksiyonel iletişim formu
- **Portfolio Yönetimi**: Projeler, yetenekler, eğitim ve deneyim bilgileri
- **SEO Dostu**: Meta etiketleri ve optimize edilmiş yapı

## 🛠️ Teknolojiler

- **Backend**: Django 5.2.5
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap 5
- **Veritabanı**: SQLite (geliştirme), PostgreSQL (production)
- **Animasyonlar**: AOS (Animate On Scroll)
- **İkonlar**: Font Awesome 6
- **Fontlar**: Google Fonts (Inter)

## 📋 Gereksinimler

- Python 3.8+
- pip
- virtualenv (önerilen)

## 🚀 Kurulum

1. **Projeyi klonlayın:**
```bash
git clone <repository-url>
cd personal_website
```

2. **Virtual environment oluşturun:**
```bash
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# veya
venv\Scripts\activate  # Windows
```

3. **Bağımlılıkları yükleyin:**
```bash
pip install -r requirements.txt
```

4. **Veritabanını hazırlayın:**
```bash
python manage.py makemigrations
python manage.py migrate
```

5. **Örnek verileri yükleyin:**
```bash
python manage.py load_sample_data
```

6. **Superuser oluşturun:**
```bash
python manage.py createsuperuser
```

7. **Sunucuyu başlatın:**
```bash
python manage.py runserver
```

8. **Tarayıcıda açın:**
```
http://127.0.0.1:8000/
```

## 📁 Proje Yapısı

```
personal_website/
├── personal_website/          # Ana proje ayarları
│   ├── settings.py           # Django ayarları
│   ├── urls.py               # Ana URL yapılandırması
│   └── wsgi.py               # WSGI yapılandırması
├── portfolio/                # Ana uygulama
│   ├── models.py             # Veritabanı modelleri
│   ├── views.py              # View fonksiyonları
│   ├── forms.py              # Form sınıfları
│   ├── admin.py              # Admin panel yapılandırması
│   └── urls.py               # URL yönlendirmeleri
├── templates/                # HTML şablonları
│   ├── base.html             # Ana şablon
│   └── portfolio/            # Portfolio şablonları
│       ├── home.html         # Ana sayfa
│       ├── about.html        # Hakkımda sayfası
│       ├── projects.html     # Projeler sayfası
│       └── contact.html      # İletişim sayfası
├── static/                   # Statik dosyalar
│   ├── css/                  # CSS dosyaları
│   ├── js/                   # JavaScript dosyaları
│   └── images/               # Resim dosyaları
├── media/                    # Yüklenen dosyalar
├── manage.py                 # Django yönetim scripti
└── README.md                 # Bu dosya
```

## 🎨 Sayfalar

### Ana Sayfa (/)
- Hero section ile tanıtım
- Hakkımda özeti
- Yetenekler
- Öne çıkan projeler
- İletişim formu

### Hakkımda (/about/)
- Detaylı hakkımda bilgileri
- Eğitim geçmişi
- İş deneyimleri
- Yetenekler listesi

### Projeler (/projects/)
- Tüm projelerin listesi
- Proje detayları
- Teknoloji stack'leri
- GitHub ve canlı demo linkleri

### İletişim (/contact/)
- İletişim formu
- İletişim bilgileri
- Sosyal medya linkleri
- SSS bölümü

## 🔧 Admin Paneli

Admin paneline erişmek için:
```
http://127.0.0.1:8000/admin/
```

### Yönetilebilir İçerikler:
- **About**: Kişisel bilgiler
- **Education**: Eğitim geçmişi
- **Experience**: İş deneyimleri
- **Skills**: Yetenekler
- **Projects**: Projeler
- **Contact**: Gelen mesajlar

## 📱 Responsive Tasarım

Website tüm cihazlarda optimize edilmiştir:
- Desktop (1200px+)
- Tablet (768px - 1199px)
- Mobile (767px ve altı)

## 🎯 Özelleştirme

### Renk Teması
CSS değişkenleri ile kolayca özelleştirilebilir:
```css
:root {
    --primary-color: #2563eb;
    --secondary-color: #1e40af;
    --accent-color: #3b82f6;
    --text-color: #1f2937;
    --light-text: #6b7280;
    --bg-color: #ffffff;
    --light-bg: #f8fafc;
    --border-color: #e5e7eb;
}
```

### İçerik Güncelleme
Admin panelinden kolayca içerik güncelleyebilirsiniz:
1. Admin paneline giriş yapın
2. İlgili bölümü seçin
3. İçeriği güncelleyin
4. Kaydedin

## 🚀 Deployment

### Production Ayarları
1. `settings.py` dosyasında `DEBUG = False` yapın
2. `ALLOWED_HOSTS` listesine domain adınızı ekleyin
3. `SECRET_KEY`'i güvenli bir değerle değiştirin
4. Statik dosyaları toplayın: `python manage.py collectstatic`
5. Veritabanını PostgreSQL'e geçirin (önerilen)

### Önerilen Hosting Platformları:
- Heroku
- DigitalOcean
- AWS
- Vercel (statik dosyalar için)

## 🤝 Katkıda Bulunma

1. Fork yapın
2. Feature branch oluşturun (`git checkout -b feature/AmazingFeature`)
3. Değişikliklerinizi commit edin (`git commit -m 'Add some AmazingFeature'`)
4. Branch'inizi push edin (`git push origin feature/AmazingFeature`)
5. Pull Request oluşturun

## 📄 Lisans

Bu proje MIT lisansı altında lisanslanmıştır.

## 📞 İletişim

- **Ad**: Talha Colfaoğlu
- **E-posta**: talha@example.com
- **GitHub**: [@talhacolfaoglu](https://github.com/talhacolfaoglu)
- **LinkedIn**: [talhacolfaoglu](https://linkedin.com/in/talhacolfaoglu)

## 🙏 Teşekkürler

- [Django](https://www.djangoproject.com/) - Web framework
- [Bootstrap](https://getbootstrap.com/) - CSS framework
- [Font Awesome](https://fontawesome.com/) - İkonlar
- [AOS](https://michalsnik.github.io/aos/) - Animasyonlar

---

⭐ Bu projeyi beğendiyseniz yıldız vermeyi unutmayın!
# projectone
