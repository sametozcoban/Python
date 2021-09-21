import math
import time

class Computer():
    def __init__(self,computer_model="",computer_durum="Kapalı",computer_hesap_makinasi=0,computer_fotograf_kırpma="Kapalı",computer_ses=0):
        print("İnit fonksiyonu çalışıyor.")
        self.computer_model=computer_model

        self.computer_durum=computer_durum

        self.computer_hesap_makinasi=computer_hesap_makinasi

        self.computer_fotograf_kırpma=computer_fotograf_kırpma

        self.computer_ses=computer_ses
    def model(self):
        computer_model=input("Laptop Modelinizi Giriniz:")
    def pc_acma(self):

        if(self.computer_durum=="Kapalı"):
            giriniz=int(input("Açmak İçin 1 ya Basınız"))
            if(giriniz==1):#kullanıcından değer alınacak.....
                self.computer_durum="Açık"
                print("Bilgisayarınız Açılıyor:")
        else:
            print("Geçersiz İşlem")
    def calculator(self):

        while True:
            print("""******************************
                        İşlem Seçiniz:
            
                        1=Toplama
            
                        2=Çıkarma
            
                        3=Bölme
            
                        4=Kuvvet Alma
        
                *********************************""")
            operation=int(input("Operasyon Seçiniz :"))

            x=int(input("1.Sayı Giriniz....."))

            y=int(input("2.Sayı Giriniz....."))

            if(operation==1):
                time.sleep(1)
                self.computer_hesap_makinasi +=x+y
                print("Toplama Sonucu:",self.computer_hesap_makinasi)
            elif(operation==2):
                time.sleep(1)
                self.computer_hesap_makinasi +=(x-y)
                print("Çıkarma Sonucu:",self.computer_hesap_makinasi)

            elif(operation==3):
                time.sleep(1)
                self.computer_hesap_makinasi +=x/y
                print("Bölme Sonucu:",self.computer_hesap_makinasi)
            elif(operation==4):
                time.sleep(1)
                self.computer_hesap_makinasi +=math.pow(x,y)
                print("Toplam:",self.computer_hesap_makinasi)
            break

    def kırpma(self):

        if(self.computer_fotograf_kırpma=="Kapalı"):
            giriniz=input("Fotoğraf Kırpmayı açmak için Q ya basınız.....")
            if(giriniz=="q"):
                print("Fotoğraf Kırpma Açılıyor....")
                self.computer_fotograf_kırpma="Açık"
        else:
            print("Fotoğraf Kırpma Zaten Kapalı")

    def comp_ses(self):
        cevap =  input("Sesi Azalt: '<'\nSesi Artır: '>'\nÇıkış : çıkış")
        while True:
            if (cevap == "<"):
                if (self.computer_ses != 0):

                    self.computer_ses -= 1
                    print("Ses:",self.computer_ses)
            elif (cevap == ">"):
                if (self.computer_ses != 21):

                    self.computer_ses += 1

                    print("Ses:",self.computer_ses)
            else:
                print("Ses Güncellendi:",self.computer_ses)
                break

laptop=Computer()

while True:
    print("""*************************
    
    1. Laptop Model
    
    2. Laptop On/Off
    
    3. Laptop Calculator
    
    4. Laptop Spinning Tool
    
    5. Laptop Voice    
 
    Çıkmak için 'q' ya basın.
            ****************************""")

    işlem=int(input("İşleme Seçiniz..."))


    if(işlem=="q"):
        print("Sistemden Çıkılıyor....")
    elif(işlem==1):
        laptop.model()
    elif(işlem==2):
        laptop.pc_acma()
    elif(işlem==3):
        laptop.calculator()
    elif(işlem==4):
        laptop.kırpma()
    elif(işlem==5):
        laptop.comp_ses()
    else:
        print("Geçersiz İşlem")


