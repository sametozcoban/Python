class asansor_1():
    def __init__(self,eve_durum="Duruyor",eve_agırlık=110):

        self.eve_durumu=eve_durum

        self.eve_agırlık=eve_agırlık
    def durum(self):
        print("""*************************
            
            İşlem Seçiniz
            <-Aşağı İnmek
            >-Yukarı Çıkmak

*************************""")
        yön=input("İşlem :")
        if(yön==">"):
            bina_sakini=int(input("Kilonuzu Giriniz :"))
            if(bina_sakini>self.eve_agırlık):
                self.eve_durum="Duruyor"
                print("Asansör Hareketi :",self.eve_durum)
            else:
                self.durum="Yukarı Yön "
                print("Asansör Hareketi :",self.durum)
        elif(yön=="<"):
            bina_sakini=int(input("Kilonuzu Giriniz :"))
            if(bina_sakini>self.eve_agırlık):
                self.eve_durum="Duruyor"
                print("Asansör Hareketi :",self.eve_durum)
            else:
                self.durum="Aşağı Yön "
                print("Asansör Hareketi :",self.durum)

eve=asansor_1()

while True:
    print("""******************************

        İŞLEMLER.......
        
        1-Asansör Çağır

*******************************""")

    işlem = input("İşlem: ")

    if(işlem=="1"):
        eve.durum()
