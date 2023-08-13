import tkinter as tk

# TuaPomodoroTimer adında bir sınıf tanımladım. 
# Yeni bir sınıfı tanımlıorum adına da TuaPomodoroTimer koydum.
# Bu sınıf, Pomoodoro tekniği zamanlayıcısı uygulmasını yönetecek.

class TuaPomodoroTimer:
    
    # Sınıfın başlatıcı (constructor) fonksiyonunu ekliyorum.
    # Bir sınıfı tanımladığımda bu fonkisyon otomatik olarak çağırılacak.
    # Bu fonkisyonunun içerisinde sınıfıın başlangıç durumunu ayarlıyorum.
    def __init__(self,root):
        
        # Oluşturulan arayüz penceresini saklamak için "root" adında bir değilken tanımladım.
        # Bu değişken, Tkinter arayüz nesnelerine erişmemizi sağlayacak bir referans olacak burası.
        self.root = root
        
        # Arayüz penceresinin başlığını "TUA Pomodoro Zamanlayıcısı" olarak ayarladım.
        self.root.title("TUA Pomodoro Zamanlayıcısı")
        
        # Timer'ın görüneceği etkiketi oluşturuyorum.
        # Arayüzde metin görüntülemek için "Label" nesnesini kullanıyorum. 
        # Bu nesneyi "root" penceresine ekleyerek görüntüleyeceğim.
        self.timer_label = tk.Label(root, text="25:00", font=("Helvetica",500))
        
        # Etiketi arayüze yerleştiriyorum burada ve yukarıdan, aşağıdan 15 piksel boşluk bırakıyorum. 
        self.timer_label.pack(pady=15) #padding
        
        # Başlatma düğmesi oluşturuyorum burada.
        # Arayüzde bir düğme oluşturmak "Button" nesnesini kullanıyorum.
        # Bu nesneyi "root" pencersine ekleyerek görüntüleyeceğim.
        self.start_button = tk.Button(root, text="Başlat", command=self.start_timer)
        
        # Bu düğmeyi de arayüze yerleştiriyorum.
        self.start_button.pack()
        
        # Zamanlayıcının çalışıp çalışmadığını takip etmek için bir değişken tanımlıyorum.
        # Bu değişken, zamanlayıcının durumunu tutacak ve Başlangıçta çalışmayacak.
        self.is_running = False
        
        # Kalan zamanı saniye cinsinden saklamak için bir değişken tanımlıyorum.
        # Bu değişken, geri sayım sırasındaki kalan süreyi saniye olarak saklayacak.
        self.remaining_time = 1500 # 25 dakikaya tekabül eden saniye (1500 saniye)
        
        # Timer'ı başlatmak için kullanılacak fonksiyonu yazıyorum.
        # Bu fonksiyon, başlatma düğmesine tıklandığında çağrılacak.
    def start_timer(self):
            # Zamanlayıcı çalışmıyorsa
            if not self.is_running: 
                # Zamanlayıcıyı başlatmak için "is_running" değişkenini -True- olarak ayarlıyorum kontrol ederek.
                self.is_running = True
                # Timer'i güncelleme fonkisyonunu çağırarak başlatıyoruz burada.
                self.update_timer()
                # Başlatma düğmemin metnini "Durdur" olarak değiştiriyorum.
                # Düğmeye tıklanınca "stop_timer" fonkisyonunu çağırmak için ayarlıyorum.
                self.start_button.config(text="Durdur", command=self.stop_timer)
        
        # Timer'i durdurmak için kullanılacak fonkisyonu tanımlıyorum.
        # Bu fonkisyon da sadece durdurma düğmesine tıklandığında çağrılacak.
    def stop_timer(self):
            
            # Zamanlayıcı çalışıyorsa
            if self.is_running:
                
                # Zamanlayıcıyı durdurmak için "is running" değişkenini -False- olarak ayarlıyorum.
                self.is_running = False
                
                # Durdurma düğmesinin metinini "Başlat" olarak değiştirmem gerekiyor.
                # Düğmeye tıklanınca "start_timer" fonkisyonunu çağırmak için ayarlıyorum.
                self.start_button.config(text="Başlat", command=self.start_timer)
        
        # Timer'i güncellemek için kullanacağım bir fonkisyon oluşturuyorum.
        # Bu fonkisyon, zamanlayıcının her saniye güncellenerek tutulmasını sağlayacak.
    def update_timer(self):
            
            # Zamanlayıcı çalışıyorsa
            if self.is_running:
                
                # Kalan zamanı bir saniye azaltacağım.
                self.remaining_time -= 1
                
                # Kalan zamanı dakika ve saniye cinsinden ayrıştırmam gerekiyor.
                
                minutes = self.remaining_time // 60 # Kalan süreyi dakikaya çeviriyorum.
                
                seconds = self.remaining_time % 60 # Kalan sürenin kalan saniye kısmını hesaplıyorum.
                
                # Timer etiketinin metnini güncelliyorum, "f-string" kullanarak dakika ve saniyeyeyi formatlıyorum.
                self.timer_label.config(text=f"{minutes:02}:{seconds:02}")
                
                # Zamanlayıcının sıfıra ulaştığını kontrol ediyorum.
                if self.remaining_time == 0:
                    # Timer'i durdurmak için "stop_timer" fonksiyonunu çağırıyorum.
                    self.stop_timer()
                    
                    # Kalan zamanı tekrar 25 dakika olarak ayarlamak istiyorum burada.
                    self.remaining_time = 1500
                
                # Belli bir saniye sonra tekrar bu fonksiyonu çağırarak timer'i güncelliyorum.
                self.root.after(1000, self.update_timer) # after fonkisyonu, belirtilen süre kadar bekledikten sonra belirtilen fonkisyonun çağırılmasını sağlar.
 
# Tkinter penceresini oluşturmam gerekiyor, bunu oluşturuyorum.
root = tk.Tk()

# TuaPomodoroTimer sınıfı kullanarak bir uygulama oluşturuyorum.
# Oluşturduğum uygulamanın ismini de sınıfta kullandığım isim ile aynı yapıyorum. Bu oluşturduğum sınıftan bir nesne yaratıyorum ve bu nesneyi de "root" penceresine koyuyorum.

app = TuaPomodoroTimer(root)

# Pencereyi açarak uygulamayı başlıyorum burada.
# Bu satır da Trkinter penceresinin kullanıcı etkileşimini bekleyerek herhangi bir şekilde uygulamanın kapanmadan çalışmasını sağlıyor.
root.mainloop()             