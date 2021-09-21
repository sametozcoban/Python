import time

class Asansor():
    def __init__(self, max_agırlık=1500, bakım_saat="Perşembe 10-11,Cuma 12-13",eve_durum="Duruyor",eve_hareket="Duruyor",eve_floors=[2,7,14,30],floors=range(-3,30)):

        self.max_agırlık = max_agırlık

        self.bakım_saat = bakım_saat

        self.eve_durum=eve_durum

        self.eve_hareket=eve_hareket

        self.eve_floors=eve_floors

        self.floors=floors

    def agırlık(self):

        while True:
            a = int(input("1.Kişi ağırlık:"))

            b = int(input("2.Kişi ağırlık:"))

            c = int(input("3.Kişi ağırlık:"))

            d = int(input("4.Kişi ağırlık:"))

            toplam = a + b + c + d
            maxagırlık = 1500
            if (maxagırlık >= toplam):
                print("Hareket ettir....")
                break

            else:
                print("Hareket edemessiniz....")


    def hareket(self):
        flors=list(self.eve_floors)
        f=list(self.floors)


        while True:
            print("""*************************
            
            İşlem Seçiniz
            <-Aşağı İnmek
            >-Yukarı Çıkmak

*************************""")

            yön=input("Yön Belirtiniz :")
            c1=int(input("C1 Kaçıncı Kattan Bastı: "))
            c2=int(input("C2 Kaçıncı Kattan Bastı: "))
            c3=int(input("C3 Kaçıncı Kattan Bastı: "))
            c4=int(input("C4 Kaçıncı Kattan Bastı: "))
            c5=int(input("C5 Kaçıncı Kattan Bastı: "))
            c6=int(input("C6 Kaçıncı Kattan Bastı: "))
            c7=int(input("C7 Kaçıncı Kattan Bastı: "))

            if(yön=="<"):

                self.durum="Aşağı Yön"
                print("Gelen Asansörlerin Bulundukları Katlar :",flors[1],flors[3])
                print(self.durum)
                print("Aşağı İnen Yolcular: ",c2,c3,c6,c7,"İndikleri Kat: ",0,-2,-3,0)
                flors[1]=-2
                flors[3]=-3
                print("Güncel Asansör Katları :",flors[1],flors[3])
                c8=int(input("C8 Kaçıncı Kata Gitmek İstedi:"))
                if((c8>int(flors[1]) or c8>int(flors[3]))):
                    if(c8>30):
                        self.durum="Duruyor"
                        print("Asansör :",self.durum)
                        break
                elif(c8<-3):
                    self.durum="Duruyor"
                    print("Asansör :",self.durum)
                    break
                self.durum="Yukarı Yön"
                print("Asansör :",self.durum)

            elif(yön==">"):
                self.durum="Yukarı Yön"
                print("Gelen Asansörlerin Bulundukları Katlar :",flors[2],flors[0])
                print(self.durum)
                print("Yukarı Çıkan Yolcular: ",c1,c4,c5,"İndikleri Kat: ",17,30,22)
                flors[2]=30
                flors[0]=17
                print("Güncel Asansör Katları :",flors[2],flors[0])
                c9=int(input("C9 Kaçıncı Kata Gitmek İstedi:"))
                if((c9<int(flors[0]))):
                    if(c9>30):
                        self.durum="Duruyor"
                        print("Asansör :",self.durum)
                        break
                    elif(c9<int(flors[0])and c9<int(flors[2])):
                        self.durum="Aşağıya İniyor..."
                        print("Asansör :",self.durum)
                        break
                elif(c9<-3):
                    self.durum="Duruyor"
                    print("Asansör :",self.durum)
                    break
                self.durum="Yukarı Yön"
                print("Asansör :",self.durum)
            break
    def floor(self):
        flors=list(self.eve_floors)
        print("Birinci Asansör Bulunduğu Kat: {} \nİkinci Asansör Bulunduğu Kat: {}\nÜçüncü Asansör Bulunduğu Kat: {}\nDördüncü Asansör Bulunduğu Kat: {}".format(flors[0],flors[1],flors[2],flors[3]))
    def durum(self):

        print("Birinci Asansör Durum: ",self.eve_durum)

        print("İkinci Asansör Durum: ",self.eve_durum)

        print("Üçüncü Asansör Durum: ",self.eve_durum)

        print("Dördüncü Asansör Durum: ",self.eve_durum)

    def bakım(self):

        bakımonarım = int(input("Bakım Onarımı Görmek İçin 1 e basınız: "))

        if (bakımonarım == 1):
            print("Bakım Saatleri:", self.bakım_saat)


machine =Asansor()

while True:
    print("""******************************

        İŞLEMLER.......
        
        1-Bakım Onarım
        2-Asansör Durumu
        3-Asansör Hareketi
        4-Asansör Konumları

*******************************""")

    işlem = input("İşlem: ")
    if (işlem == "q"):
        print("Çıkış Yapılıyor")
    elif (işlem == "1"):
        time.sleep(1)
        machine.bakım()
    elif(işlem=="2"):
        time.sleep(1)
        machine.durum()
    elif(işlem=="3"):
        time.sleep(1)
        machine.agırlık()
        machine.hareket()
    elif(işlem=="4"):
        machine.floor()


