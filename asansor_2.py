#Bu senayo 2 kişi ve 2 farklı asansöre uygun şekilde kodlanmıştır.
class asansor():
    def __init__(self,eve1_durum="Duruyor",eve2_durum="Duruyor",eve_hareket="Duruyor",eve_kilo=200):

        self.eve1_durum=eve1_durum

        self.eve2_durum=eve2_durum

        self.eve_hareket=eve_hareket

        self.eve_kilo=eve_kilo
    def durum(self):

        print("""*************************
            
            İşlem Seçiniz
            <-Aşağı İnmek
            >-Yukarı Çıkmak

*************************""")
        yön=input("Birinci Bina Sakini İşlem Giriniz :")
        yön1=input("İkinci Bina Sakini İşlem Giriniz :")

        if(yön==yön1 and yön==">"):
            bina_sakini_1=int(input("Birinci Kişi Kilonuzu Giriniz :"))
            bina_sakini_2=int(input("İkinci Kişi Kilonuzu Giriniz :"))
            t_kilo=bina_sakini_1+bina_sakini_2
            if(t_kilo>self.eve_kilo):
                self.eve1_durum="Duruyor"
                print("Asansör Hareketi :",self.eve1_durum)
            else:
                self.durum="Yukarı Yön "
                print("Asansör Hareketi :",self.durum)
        elif(yön==yön1 and yön=="<"):
            bina_sakini_1=int(input("1.Kişi Kilonuzu Giriniz :"))
            bina_sakini_2=int(input("2.Kişi Kilonuzu Giriniz :"))
            t_kilo=bina_sakini_1+bina_sakini_2
            if(t_kilo>self.eve_kilo):
                self.eve1_durum="Duruyor"
                print("Asansör Hareketi :",self.eve1_durum)
            else:
                self.durum="Aşağı Yön "
                print("Asansör Hareketi :",self.durum)
        elif(yön==">"):
            bina_sakini_1=int(input("Kilonuzu Giriniz :"))
            if(yön1=="<"):
                bina_sakini_2=int(input("Kilonuzu Giriniz :"))
                if(bina_sakini_2>self.eve_kilo):
                    self.eve2_durum="Duruyor"
                    print("İkinci Asansör Hareketi :",self.eve2_durum)
                else:
                    self.durum="Aşağı Yön "
                    print("İkinci Asansör Hareketi :",self.durum)
            if(bina_sakini_1>self.eve_kilo):
                self.eve1_durum="Duruyor"
                print("Birinci Asansör Hareketi :",self.eve1_durum)
            else:
                self.durum="Yukarı Yön "
                print("Birinci Asansör Hareketi :",self.durum)
        elif(yön=="<"):
            bina_sakini_1=int(input("Kilonuzu Giriniz :"))
            if(yön1==">"):
                bina_sakini_2=int(input("Kilonuzu Giriniz :"))
                if(bina_sakini_2>self.eve_kilo):
                    self.eve2_durum="Duruyor"
                    print("İkinci Asansör Hareketi :",self.eve2_durum)
                else:
                    self.durum="Yukarı Yön "
                    print("İkinci Asansör Hareketi :",self.durum)
            if(bina_sakini_1>self.eve_kilo):
                self.eve1_durum="Duruyor"
                print("Birinci Asansör Hareketi :",self.eve1_durum)
            else:
                self.durum="Aşağı Yön "
                print("Birinci Asansör Hareketi :",self.durum)




while True:
    eve=asansor()
    print("""******************************

        İŞLEMLER.......
        
        1-Asansör Çağır

*******************************""")

    işlem = input("İşlem: ")

    if(işlem=="1"):
        eve.durum()
