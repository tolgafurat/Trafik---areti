import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image
import numpy
#eğitilen modeli yüklüyoruz
from keras.models import load_model
model = load_model('./model.h5') 
#tüm trafik işaretlerini gösteren dictionary
siniflar = { 1:'Azami Hız Sınırı (20km/sa)',
           2:'Azami Hız Sınırı (30km/sa)',
           3:'Azami Hız Sınırı (50km/sa)',
           4:'Azami Hız Sınırı (60km/sa)',
           5:'Azami Hız Sınırı (70km/sa)',
           6:'Azami Hız Sınırı (80km/sa)',
           7:'Hız Limitinin Sonu (80km/sa)',
           8:'Azami Hız Sınırı (100km/sa)',
           9:'Azami Hız Sınırı (120km/sa)',
           10:'Öndeki aracı geçmek yasaktır',
           11:'Yük Taşıtlarının Öndeki Aracı Geçmesi Yasaktır',
           12:'Ana Yol-Tali Yol Kavşağı',
           13:'Anayol',
           14:'Yol Ver',
           15:'DUR',
           16:'Taşıt Trafiğine Kapalı Yol',
           17:'Kamyon Giremez',
           18:'Girişi Olmayan Yol',
           19:'Dikkat',
           20:'Sola Tehlikeli Viraj',
           21:'Sağa Tehlikeli Viraj',
           22:'Sola Tehlikeli Devamlı Virajlar',
           23:'Kasisli Yol',
           24:'Kaygan Yol',
           25:'Soldan Daralan Kaplama',
           26:'Yolda Çalışma',
           27:'Işıklı İşaret Cihazı',
           28:'Yaya Geçidi',
           29:'Çocuklar Geçebilir',
           30:'Bisiklet Geçebilir',
           31:'Gizli Buzlanma',
           32:'Vahşi Hayvan Geçebilir',
           33:'Bütün Yasaklama ve Kısıtlamaların Sonu',
           34:'İleride Sağa Mecburi Yön',
           35:'İleride Sola Mecburi Yön',
           36:'İleri Mecburi Yön',
           37:'İleri ve Sağa Mecburi Yön',
           38:'İleri ve Sola Mecburi Yön',
           39:'Sağdan Gidiniz',
           40:'Soldan Gidiniz',
           41:'Ada Etrafında Dönünüz',
           42:'Geçme Yasağı Sonu',
           43:'Yük Taşıtları ile Geçme Yasağının Sonu' }
#grafik arayüzünü oluşturuyoruz
ustKisim=tk.Tk()
ustKisim.geometry('800x600')
ustKisim.title('Trafik İşareti Sınıflandırma')
ustKisim.configure(background='#CDCDCD')
etiket=Label(ustKisim,background='#CDCDCD', font=('arial',15,'bold'))
isaretFotografi = Label(ustKisim)

def Siniflandir(dosyaKonumu):
    global label_packed
    fotograf = Image.open(dosyaKonumu)
    fotograf = fotograf.resize((30,30))
    fotograf = numpy.expand_dims(fotograf, axis=0)
    fotograf = numpy.array(fotograf)


    tahmin = model.predict(fotograf)[0]
    sinifIndexi=numpy.argmax(tahmin)#,axis=1


    print(sinifIndexi)

    
    etiket.configure(foreground='#011638', text=siniflar[sinifIndexi+1])
def SiniflandirButonuGoster(file_path):
    siniflandirB = Button(ustKisim,text="Fotoğraf Sınıflandır",command=lambda: Siniflandir(file_path),padx=10,pady=5)
    siniflandirB.configure(background='#364156', foreground='white',font=('arial',10,'bold'))
    siniflandirB.place(relx=0.79,rely=0.46)


def FotografYukle():
    try:
        dosyaKonumu = filedialog.askopenfilename()
        yuklenen = Image.open(dosyaKonumu)
        yuklenen.thumbnail(((ustKisim.winfo_width()/2.25),(ustKisim.winfo_height()/2.25)))
        foto = ImageTk.PhotoImage(yuklenen)
        isaretFotografi.configure(image=foto)
        isaretFotografi.image=foto
        etiket.configure(text='')
        SiniflandirButonuGoster(dosyaKonumu)
    except:
        pass
    
yukle = Button(ustKisim,text="Fotoğraf yükle",command=FotografYukle,padx=10,pady=5)
yukle.configure(background='#364156', foreground='white',font=('arial',10,'bold'))
yukle.pack(side=BOTTOM,pady=50)
isaretFotografi.pack(side=BOTTOM,expand=True)
etiket.pack(side=BOTTOM,expand=True)
baslik = Label(ustKisim, text="Trafik işareti kontrol et",pady=20, font=('arial',20,'bold'))
baslik.configure(background='#CDCDCD',foreground='#364156')
baslik.pack()
ustKisim.mainloop()