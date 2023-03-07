import tkinter as tk #Gerekli kütüphaneler
from tkinter import messagebox
from datetime import datetime
import csv

class Pizza:  # Pizza ust Sinifi 
    def __init__(self,cost,description):
        self.__cost = cost #kapsuleme islemi
        self.__description = description
        
    def get_cost(self): #kapsullemden dolayi fonskiyonlarin olusturulması
        return self.__cost
    
    def get_description(self):
        return self.__description

#Pizza tabanlarinin siniflari olusturulmasi
class Klasik(Pizza):
    def __init__(self):
        cost = 80 # pizzanin fiyat ve ozellikleri tanimlanmasi
        description = "Klasik Pizza"
        Pizza.__init__(self, cost, description)  # pizza sinifindan miras alma
    
class Margarita(Pizza):
    def __init__(self):
        cost = 85 
        description = "Margarita Pizza"
        Pizza.__init__(self, cost, description)
        
class TurkPizza(Pizza):
    def __init__(self):
        cost = 90
        description = "Turk Pizza"
        Pizza.__init__(self, cost, description)

class Sade(Pizza):
    def __init__(self):
        cost = 75 
        description = "Sade Pizza"
        Pizza.__init__(self, cost, description)
class Bos(Pizza):
    def __init__(self):
        cost = 0 
        description = ""
        Pizza.__init__(self, cost, description)
        
#Decorator ust sinifin tanimlanmasi
class Decorator(Pizza):
    def __init__(self,component, cost,  description):
        self.component = component
        self.__cost = cost #kapsülleme islemi
        self.__description = description
        Pizza.__init__(self, cost, description)#pizza sinifindan miras alma
        
    def get_cost(self):
        return self.component.get_cost() + Pizza.get_cost(self)#pizza ve ek malzemelerin fiyatinin toplanmasi
   
    def get_description(self):
        return self.component.get_description() + ' ' + Pizza.get_description(self)#pizza ve ek malzemelerin özelliklerinin yazilmasi

#Ek Malzemelerin siniflarin tanimlanmasi      
class Zeytin(Decorator):
    def __init__(self,component):
        cost = 5#fiyat ve özellikleri tanimlanmasi
        description = "Zeytinli"
        Decorator.__init__(self, component, cost, description)# Decorater sinifindan miras alma
        
class Mantar(Decorator):
    def __init__(self,component):
        cost = 7
        description = "Mantarli"
        Decorator.__init__(self, component, cost, description)

class KeciPeynir(Decorator):
    def __init__(self,component):
        cost = 10
        description = "Keci Peynirli"
        Decorator.__init__(self, component, cost, description)
        
class Et(Decorator):
    def __init__(self,component):
        cost = 15
        description = "Etli"
        Decorator.__init__(self, component, cost, description)

class Sogan(Decorator):
    def __init__(self,component):
        cost = 3
        description = "Soganli"
        Decorator.__init__(self, component, cost, description)

class Misir(Decorator):
    def __init__(self,component):
        cost = 4
        description = "Misirli "
        Decorator.__init__(self, component, cost, description)
   
#tkinter uygulama sinifinin olusturulmasi
class PizzaApp():
    def __init__(self):
        bgAll ='#eee7c4' # uygulamanin ana tema renklerinin tanimlanmasi
        fgAll="#003049"
        
        self.root = tk.Tk() #tkinter uygulamasi olusturulmasi
        self.root.geometry("700x450+80+100") #pencerenin boyutu ve konumunun ayarlanmasi
        self.root.title("Pizza Siparis Uygulamasi") #pencereye ad verilmesi
        self.root.configure(bg=bgAll) #pencerinin arkaplani degistirilmesi
        
        menuLabel = tk.Label(self.root,text="🍕 Pizza Sipariş Sistemi 🍕", bg ="#e75414", fg="black",font="Arial 24 bold")
        menuLabel.pack(pady=10) #ana baslik labeli taninmasi
        
        pizzaTabanLabel = tk.Label(self.root,text="Lütfen Bir Pizza Tabanı Seçiniz :",font="Arial 11 italic bold",bg = bgAll,fg=fgAll)
        pizzaTabanLabel.pack(pady= 5,anchor="w",padx=5) 

        self.tabanDegiskeni = tk.StringVar() #radio buton için degisken tanimlanmasi
        self.tabanDegiskeni.set(None) #degiskenin degeri sifirlanmasi
        
        # for dongüsü icin liste tanimlanmasi ve dinamik fiyatlarin ekranda gösterilmesi icin pizza classi kullanilmasi
        pizzaDegiskenleri = [("Klasik Pizza  (" + str(Klasik().get_cost()) +" ₺)","klasik"),
                             ("Margarita Pizza  (" + str(Margarita().get_cost()) + " ₺)","margarita"),
                             ("Türk Pizza  (" + str(TurkPizza().get_cost()) + " ₺)","turkpizza"),
                             ("Sade Pizza  (" + str(Sade().get_cost()) + " ₺)","sade")]

        for text, value in pizzaDegiskenleri: #for dongusu ile radio butonlarin ekrana yerlestirilmesi
            pizzaRadioButon = tk.Radiobutton(self.root, text= text, variable = self.tabanDegiskeni, value=value,bg = bgAll,font="Arial 10 italic")
            pizzaRadioButon.pack(anchor="w",padx=10)

        sosLabel = tk.Label(self.root,text="Lütfen İstediğiniz Ek Malzemeleri Seçin :",font="Arial 11 italic bold",bg =bgAll, fg=fgAll)
        sosLabel.pack(pady=5,anchor="w",padx=5)

        self.sosDegerListesi = [] # secilen ek malzemeleri icin bos liste olusturulmasi
        #for dongusu icin ek malzeme listesi tanimlanmasi ve dinamik fiyatlarin ekranda gosterilmesi pizza classi kullanilmasi
        sosDegiskenleri = [("Zeytin (+" + str(Zeytin(Bos()).get_cost()) + " ₺)","zeytin"),  
                           ("Mantar (+" + str(Mantar(Bos()).get_cost()) + " ₺)","mantar"),        
                           ("Keçi Peyniri (+" + str(KeciPeynir(Bos()).get_cost()) + " ₺)","peynir"),       
                           ("Et (+" + str(Et(Bos()).get_cost()) + " ₺)"  ,"et"),            
                           ("Soğan (+" + str(Sogan(Bos()).get_cost()) + " ₺)","sogan"),      
                           ("Mısır (+" + str(Misir(Bos()).get_cost()) + " ₺)","misir")]

        # Frame oluşturma
        frame = tk.Frame(self.root,bg= bgAll)
        frame.pack(anchor="w")

        # Checkbox'ları grid yöntemiyle düzenleme
        for i, (text, value) in enumerate(sosDegiskenleri): # for dongusu ile checkboxlarin olusturulmasi
            self.sosDegiskeni = tk.BooleanVar() #checkboxlar icin degiken tanimlanmasi
            sosCheckButon = tk.Checkbutton(frame, text=text, variable= self.sosDegiskeni, font="Arial 10 italic", bg=bgAll, anchor="w")
            sosCheckButon.grid(row=i//2, column=i%2, padx=10, pady=2, sticky="w") # grid yontemiyle ücer'li bloklar halinde  ekrana yerlestirme 
            self.sosDegerListesi.append((self.sosDegiskeni, value))

        self.ucretLabel =tk.Label(self.root,text=" Toplam Ücret  = ",font=("Arial 12 italic bold"),bg= bgAll,fg= fgAll)
        self.ucretLabel.pack(pady=8,padx=8,anchor="w") #toplam ucret pencereye yazdirilmasi

        # Frame oluşturma
        frame = tk.Frame(self.root,bg=bgAll)
        frame.pack(side="top", fill="x")
    
        cıkısButon = tk.Button(frame,text="Çıkış",font="Arial 12 italic",bg="#362E41",fg = "white",command= self.root.destroy)
        cıkısButon.pack(side="left", padx=10, pady=1) #cikis butonunun olusturma

        self.siparisButon = tk.Button(frame,text="Sipariş Ver ",font="Arial 14 italic",bg="#D62828",command=self.odemeSayfasi ,fg = "white",state="disabled")
        self.siparisButon.pack(side="right", padx=25, pady=1) #siparis ver butonun olusturulmasi

        hesapButon = tk.Button(frame, text="Ücret Hesapla",font="Arial 13 italic",bg="#362E41",fg = "white",command=self.ucretHesapla)      
        hesapButon.pack(side="right", padx=10, pady=18) #ucret hesapla butonun olusturulmasi
        
        self.root.mainloop()  
    
    def ucretHesapla(self): #ucrethesaplama fonksiyonun tanimlanmasi
        tabanDegiskeni = self.tabanDegiskeni.get() 
        
        if tabanDegiskeni == "klasik": #radio butonlarin degerlerine gore pizza classlarin tanimlanmasi
            self.pizzam = Klasik()
            
        elif tabanDegiskeni == "margarita":
            self.pizzam = Margarita()
            
        elif tabanDegiskeni == "turkpizza":
            self.pizzam = TurkPizza()
            
        elif tabanDegiskeni == "sade":
            self.pizzam = Sade()
            
        for self.sosDegiskeni, value in self.sosDegerListesi:
             if self.sosDegiskeni.get():

                 try: #try komutu ile secim olmassa hata vermemesini engelleme
                     if value == "zeytin":
                         self.pizzam = Zeytin(self.pizzam)
                         
                     elif value == "mantar":
                         self.pizzam = Mantar(self.pizzam)
                         
                     elif value == "peynir":
                         self.pizzam = KeciPeynir(self.pizzam)
                         
                     elif value == "et":
                         self.pizzam = Et(self.pizzam)
                         
                     elif value == "sogan":
                         self.pizzam = Sogan(self.pizzam)
                         
                     elif value == "misir":
                         self.pizzam = Misir(self.pizzam)
                 except:
                     pass
        try: #hata almamak ıcın try komutu kullanmak  
            self.ucretLabel.config(text=(" Toplam Ücret  = "+ str(self.pizzam.get_cost()) + " ₺") )
            self.siparisButon.configure(state="normal") #pencereye hesaplanan fiyati yazdirilmasi

        except:
            pass

    def odemeSayfasi(self): #odeme sayfasi olusturulmasi
        self.siparisButon.configure(state="disabled") # siparid butonunun pasif olmasi

        bg = "#8cb1c3" #ana tema renklerin tanimlanmasi
        fg = "white"
        
        self.pencere = tk.Tk() #pencere olusturulmasi
        self.pencere.title("Ödeme Ekranı") #pencere adi olusturulmasi
        self.pencere.geometry("600x400+782+150") #pencerenin boyutu ve konumu olusturulmasi
        self.pencere.configure(bg="#8cb1c3") #pencerenin arkaplanin degistirilmesi

        menuLabel = tk.Label(self.pencere ,text=" Ödeme Ekranı ", bg = "#003049", fg="white",font="Arial 15 italic bold")
        menuLabel.grid(pady=15, row =0,column=0,columnspan=2) #ana baslik labeli olusturma
       
        #kullanicidan istenilen bilgilerin girmesi icin entryler olusturulmasi
        isimLabel = tk.Label(self.pencere,text="Ad Soyad :",font="Arial 11 bold",bg = bg,fg = fg)
        isimLabel.grid(pady= 10,row=1, column=0,padx=10)
       
        self.entry = tk.Entry(self.pencere,width=30)
        self.entry.grid(pady= 10,row=1, column=1,padx=10)
       
        telefonLabel = tk.Label(self.pencere,text="Telefon Numarasi :",font="Arial 11 bold",bg = bg,fg = fg)
        telefonLabel.grid(pady= 10,row=2, column=0,padx=10)
       
        self.entry2 = tk.Entry(self.pencere,width=30)
        self.entry2.grid(pady= 10,row=2, column=1,padx=10)
       
        adresLabel = tk.Label(self.pencere,text="Adres :",font="Arial 11 bold", bg = bg, fg = fg)
        adresLabel.grid(pady= 10,row=3, column=0,padx=10)
       
        self.entry3 = tk.Entry(self.pencere,width=30)
        self.entry3.grid(pady= 10,row=3, column=1,padx=10)
       
        kartNoLabel = tk.Label(self.pencere,text="Kart Numarası :",font="Arial 11 bold",bg = bg,fg = fg)
        kartNoLabel.grid(pady= 10,row=4, column=0,padx=10)
       
        self.entry4 = tk.Entry(self.pencere,width=30)
        self.entry4.grid(pady= 10,row=4, column=1,padx=10)
       
        def onaylandi(): #buton icin onaylama fonksiyonu olusturulmasi
            siparisOlusturmaButon.config(state=tk.NORMAL)
            onayButon.config(text="Onaylandı")
        
        def iptal(): #buton icin iptal fonksiyonu olusturulmasi
            cevap = tk.messagebox.askquestion(title="Emin Misiniz?",message="Siparişi İptal Etmek İsteğinize Emin Misiniz ?") #ekrana soru widgeti cikmasi
            siparisOlusturmaButon.config(state=tk.DISABLED)
            onayButon.config(text="Onayla")

            if cevap == "yes":
                self.pencere.destroy() #kullanici eveti secerse odeme ekraninin kapanmasi
            else:
                pass
        
        #gerekli labellarin olusturulmasi
        bilgiLabel = tk.Label(self.pencere,text="Sipariş İçeriği  = ",font="Arial 10 italic bold underline",fg = fg ,bg = bg)
        bilgiLabel.grid(row=5,column=0,sticky= tk.E,padx=10)
        
        bilgiLabel1 = tk.Label(self.pencere,text= self.pizzam.get_description() ,font="Arial 10 italic bold",fg = fg ,bg = bg)
        bilgiLabel1.grid(row=5,column=1,sticky=tk.W)
        
        bilgiUcretLabel = tk.Label(self.pencere,text= "Toplam Ücret  =  ",font="Arial 10 italic bold underline",fg = fg ,bg = bg)
        bilgiUcretLabel.grid(row=6,column=0,sticky= tk.E,padx=8)
        
        bilgiUcretLabel1 = tk.Label(self.pencere,text= str(self.pizzam.get_cost())+ " TL",font="Arial 10 italic bold ",fg = fg ,bg = bg)
        bilgiUcretLabel1.grid(row=6,column=1,sticky=tk.W)
        
        onayLabel = tk.Label(self.pencere, text="*Bilgilerin doğruluğunu onaylıyorum",font="Arial 11 italic",bg=bg,fg=fg)
        onayLabel.grid(pady=10,row=7, column=1,columnspan=2,padx=1)

        onayButon = tk.Button(self.pencere, text="Onayla", command=onaylandi,bg= "#619b8a",fg=fg)
        onayButon.grid( padx=10,row=7, column=0,pady=10) #onayla butonunun olusturulmasi
        
        iptalButon = tk.Button(self.pencere, text="İptal", command=iptal ,bg = "#f94144",fg=fg)
        iptalButon.grid( padx=10,row=8, column=0) #iptal butonunun olustutulmasi
        
        siparisOlusturmaButon = tk.Button(self.pencere, text="SİPARİŞ VER", state=tk.DISABLED,command=self.bilgiKaydet,font="Arial 12 bold",bg = "#277da1",fg=fg)
        siparisOlusturmaButon.grid(padx=10,row=8, column=1) #siparis ver butonunun olsuturulmasi
        
        self.pencere.mainloop()
        
    def bilgiKaydet(self): #bilgi kaydetmek icin fonksiyon olusturulmasi
        adSoyad = self.entry.get() #kullanicidan alinan verilerin alinmasi
        telNo = self.entry2.get()
        adres = self.entry3.get()
        kartNo = self.entry4.get()

        suan = datetime.now() #tarih ve saatin alinmasi
        tarih = datetime.strftime(suan, "%d-%m-%Y %B %A %H:%M:%S")

        with open('Orders_Database.csv', mode='a', newline='') as file: #csv dosyasina verilerin yazdirilmasi
            writer = csv.writer(file)
            writer.writerow([tarih,adSoyad,telNo,adres,kartNo,self.pizzam.get_description(),self.pizzam.get_cost()])

        #ekrana bilgi sayfasi gelmesi
        messagebox.showinfo(title="🍕🍕🍕Sipariş Onay🍕🍕🍕",message= "SİPARİŞİNİZ ONAYLANDI . Kartınızdan yalnız ' " + str(self.pizzam.get_cost()) 
                            + " 'TL çekilmiştir."+ "\nSiparişiniz En Kısa Sürede Teslim Edilecektir. \nBizi Tercih Ettiğiniz için Teşekkür Ederiz.🍕")

        self.pencere.destroy()

def main(): #main fonksiyonun olusturulmasi
    PizzaApp() # tkinter uygulama sinifin cagrilmasi

if __name__ == "__main__":
    main() #main fonksiyonun cagrilmasi