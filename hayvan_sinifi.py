class animals():
    def __init__(self,tur,takim,yas,cinsiyet):

        self.tur=tur
        self.takim=takim
        self.yas=yas
        self.cinsiyet=cinsiyet
    def bilgilerigoster(self):
        print("animals bigileri :")
        print("Tur: {}\nTakim: {}\nYas: {}\nCinsiyet: {}".format(self.tur,self.takim,self.yas,self.cinsiyet))

class dog(animals):
    def __init__(self,tur,takim,yas,cinsiyet):
        super().__init__(tur,takim,yas,cinsiyet)
        print("Horse fonksiyonuna girildi...")
    def bilgilerigoster(self):
        print("Dog bilgileri ")

        print("Tur: {}\nTakim: {}\nYas: {}\nCinsiyet: {}".format(self.tur,self.takim,self.yas,self.cinsiyet))

class bird(animals):
    def __init__(self,tur,takim,yas,cinsiyet):
        super().__init__(tur,takim,yas,cinsiyet)
        print("Bird fonksiyonuna girildi...")
    def bilgilerigoster(self):
        print("Bird bilgileri ")

        print("Tur: {}\nTakim: {}\nYas: {}\nCinsiyet: {}".format(self.tur,self.takim,self.yas,self.cinsiyet))
class horse(animals):
    def __init__(self,tur,takim,yas,cinsiyet):
        super().__init__(tur,takim,yas,cinsiyet)
        print("Horse fonksiyonuna girildi...")
    def bilgilerigoster(self):
        print("Horse bilgileri ")

        print("Tur: {}\nTakim: {}\nYas: {}\nCinsiyet: {}".format(self.tur,self.takim,self.yas,self.cinsiyet))


a=dog("Pitbull","KÖpek",2,"Erkek")
b=bird("Atmaca","Yabani Kuş",1,"Dişi")
c=horse("Saf Afgan","Afgan",2,"Erkek")


while True:
    print("""******************
    
    1-Dog
    
    2-Bird
    
    3-Animals
    
            ********************""")
    print(("Çıkış yapmak istiyorsanız q'basınız..."))
    sayı=input("Lütfen Sayı Gİriniz:")

    if(sayı=="q"):
        print("Çıkış Yapılıyor...")

    if(sayı=="1"):

        print("Dog Yaşı:",a.yas)
        print("Dog Türü:",a.tur)
        print("Dog Takımı:",a.takim)
        print("Dog Cinsiyet",a.cinsiyet)
        print(a.bilgilerigoster())
    elif(sayı=="2"):

        print("Bird Yaşı:",b.yas)
        print("Bird Türü:",b.tur)
        print("Bird Takımı:",b.takim)
        print("Bird Cinsiyet",b.cinsiyet)
        print(b.bilgilerigoster())
    elif(sayı=="3"):

        print("Horse Yaşı:",c.yas)
        print("Horse Türü:",c.tur)
        print("Horse Takımı:",c.takim)
        print("Horse Cinsiyet",c.cinsiyet)
        print(c.bilgilerigoster())

    else:
        break




