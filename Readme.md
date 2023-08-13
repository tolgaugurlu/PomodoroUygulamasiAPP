# TUA Pomodoro Zamanlayıcısı

Bu proje, Pomodoro tekniğini uygulayan basit bir zamanlayıcı uygulamasıdır. Pomodoro tekniği, çalışma ve mola sürelerini sık sık sırayla uygulayarak verimliliği artırmayı amaçlayan bir zaman yönetimi tekniğidir.

## Özellikler

- 25 dakika çalışma süresi ve 5 dakika mola süresi ile Pomodoro tekniğini uygular.
- Kullanıcı başlatma ve durdurma düğmeleri ile zamanlayıcıyı kontrol edebilir.
- Geri sayım süresi dakika ve saniye olarak görüntülenir.
- Otomatik olarak çalışma ve mola sürelerini sırayla takip eder.

## Nasıl Kullanılır

1. Proje dosyalarını bilgisayarınıza indirin veya klonlayın.
2. `main.py` dosyasını çalıştırın.
3. Açılan arayüzde "Başlat" düğmesine tıklayarak zamanlayıcıyı başlatın.
4. Çalışma süresi boyunca geri sayım süresi dakika ve saniye olarak görüntülenecektir.
5. Çalışma süresi sona erdiğinde, zamanlayıcı otomatik olarak 5 dakikalık bir mola süresine geçecektir.
6. Mola süresi sona erdiğinde tekrar çalışma süresine geçecektir.
7. "Durdur" düğmesine tıklayarak zamanlayıcıyı istediğiniz zaman durdurabilirsiniz.

## Gereksinimler

Bu projeyi çalıştırmak için [Python](https://www.python.org/) ve [Tkinter](https://docs.python.org/3/library/tkinter.html) kütüphanesi gereklidir. Genellikle Python'ın son sürümüyle birlikte Tkinter otomatik olarak gelir.

## Kod Açıklaması

Bu projenin kaynak kodu, Tkinter kütüphanesini kullanarak bir Pomodoro zamanlayıcısı oluşturur. Aşağıda kodun ana bileşenleri açıklanmıştır:

- `TuaPomodoroTimer` sınıfı: Pomodoro zamanlayıcısını yöneten ana sınıftır. Tkinter arayüzünü oluşturur, düğmeleri yönetir ve geri sayım süresini günceller.

- `start_timer` fonksiyonu: Pomodoro zamanlayıcısını başlatmak için kullanılır. Zamanlayıcı zaten çalışmıyorsa, çalışma durumunu başlatır ve düğme metnini "Durdur" olarak değiştirir.

- `stop_timer` fonksiyonu: Pomodoro zamanlayıcısını durdurmak için kullanılır. Zamanlayıcı çalışıyorsa, çalışma durumunu durdurur ve düğme metnini "Başlat" olarak değiştirir.

- `update_timer` fonksiyonu: Pomodoro zamanlayıcısının geri sayım süresini günceller. Süre sıfıra ulaştığında, zamanlayıcıyı durdurur ve çalışma/mola süresini sırayla takip etmek için gerekli ayarlamaları yapar.
