import time

class asansor():
    def __init__(self,eve_1_konum=25,eve_2_konum=21,eve_3_konum=12,eve_1_hareket="Duruyor",eve_2_hareket="Duruyor",eve_3_hareket="Duruyor",eve_kilo=200):
        self.eve_1_konum=eve_1_konum

        self.eve_2_konum=eve_2_konum

        self.eve_3_konum=eve_3_konum

        self.eve_1_hareket=eve_1_hareket

        self.eve_2_hareket=eve_2_hareket

        self.eve_3_hareket=eve_3_hareket

        self.eve_kilo=eve_kilo
    def hareket(self):

        button=input("Push Button :")
        button_1=input("Push Button :")

        if(button==button_1 and button==">"):
            katlar=[self.eve_1_konum,self.eve_2_konum,self.eve_3_konum]
            uzaklıklar=[]
            for i in katlar:
                a=i
                uzaklıklar.append(a)
            if(min(uzaklıklar)==self.eve_1_konum):
                self.eve_1_hareket="Aşağıya İniyor"

                print("1.Asansör Aşağıya İniyor")
            elif(min(uzaklıklar)==self.eve_2_konum):
                self.eve_2_hareket="Aşağıya İniyor"

                print("2.Asansör Aşağıya İniyor")
            elif(min(uzaklıklar)==self.eve_3_konum):
                self.eve_3_hareket="Aşağıya İniyor"

                print("3..Asansör Aşağıya İniyor")

            user_1=int(input("Lütfen Kilonuzu Giriniz :"))

            user_2=int(input("Lütfen Kilonuzu Giriniz :"))

            t_kilo=user_1+user_2

            time.sleep(2)

            if(t_kilo<self.eve_kilo):
                if(min(uzaklıklar)==self.eve_1_konum):
                    self.eve_1_hareket="Geliyor"
                    time.sleep(1)
                    print("1.Asansör :",self.eve_1_hareket)
                    time.sleep(1)
                    self.eve_1_hareket="Yukarı Çıkıyor"
                    print("1.Asansör :",self.eve_1_hareket)
                elif(min(uzaklıklar)==self.eve_2_konum):
                    self.eve_2_hareket="Geliyor"
                    time.sleep(1)
                    print("2.Asansör :",self.eve_2_hareket)
                    time.sleep(1)
                    self.eve_2_hareket="Yukarı Çıkıyor"
                    print("2.Asansör :",self.eve_2_konum)
                elif(min(uzaklıklar)==self.eve_3_konum):
                    self.eve_3_hareket="Geliyor"
                    time.sleep(1)
                    print("3.Asansör :",self.eve_3_hareket)
                    self.eve_3_hareket="Yukarı Çıkıyor"
                    print("3.Asansör :",self.eve_3_hareket)
            elif(t_kilo>self.eve_kilo):
                if(min(uzaklıklar)==self.eve_1_konum):
                    self.eve_1_konum="Duruyor"
                    print("1.Asansör :",self.eve_1_konum)
                elif(min(uzaklıklar)==self.eve_2_konum):
                    self.eve_2_konum="Duruyor"
                    print("2.Asansör :",self.eve_2_konum)
                elif(min(uzaklıklar)==self.eve_3_konum):
                    self.eve_3_konum="Duruyor"
                    print("3.Asansör :",self.eve_3_konum)

            button_3=input("Push Button")
            if(button_3 == "<"):
                user_3=int(input("Kilonuzu Giriniz :"))
                if(self.eve_1_hareket=="Duruyor" or "Duruyor"==self.eve_2_hareket or "Duruyor"==self.eve_3_hareket):
                    uzaklıklar.remove(min(uzaklıklar))
                    if(min(uzaklıklar)==self.eve_1_konum):
                        self.eve_1_hareket="Geliyor"
                        print("1.Asansör :",self.eve_1_hareket)
                        if(user_3>self.eve_kilo):
                            self.eve_1_hareket="Duruyor"
                            print("1.Asansör :",self.eve_1_hareket)
                        else:
                            self.eve_1_hareket="Aşağıya İniyor"
                            print("1.Asansör :",self.eve_1_hareket)
                    elif(min(uzaklıklar)==self.eve_2_konum):
                        self.eve_2_hareket="Geliyor"
                        print("2.Asansör :",self.eve_2_hareket)
                        if(user_3>self.eve_kilo):
                            self.eve_2_hareket="Duruyor"
                            print("2.Asansör :",self.eve_2_hareket)
                        else:
                            self.eve_2_hareket="Aşağıya İniyor"
                            print("2.Asansör :",self.eve_2_hareket)
                    elif(min(uzaklıklar)==self.eve_3_konum):
                        self.eve_2_hareket="Geliyor"
                        print("3.Asansör :",self.eve_3_hareket)
                        if(user_3>self.eve_kilo):
                            self.eve_3_hareket="Duruyor"
                            print("3.Asansör :",self.eve_3_hareket)
                        else:
                            self.eve_3_hareket="Aşağıya İniyor"
                            print("3.Asansör :",self.eve_3_hareket)
        elif(button==button_1 and button=="<"):
            katlar=[self.eve_1_konum,self.eve_2_konum,self.eve_3_konum]
            uzaklıklar=[]
            for i in katlar:
                a=i
                uzaklıklar.append(a)
            if(min(uzaklıklar)==self.eve_1_konum):
                self.eve_1_hareket="Aşağıya İniyor"

                print("1.Asansör Aşağıya İniyor")
            elif(min(uzaklıklar)==self.eve_2_konum):
                self.eve_2_hareket="Aşağıya İniyor"

                print("2.Asansör Aşağıya İniyor")
            elif(min(uzaklıklar)==self.eve_3_konum):
                self.eve_3_hareket="Aşağıya İniyor"

                print("3.Asansör Aşağıya İniyor")

            user_1=int(input("Lütfen Kilonuzu Giriniz :"))

            user_2=int(input("Lütfen Kilonuzu Giriniz :"))

            t_kilo=user_1+user_2

            time.sleep(2)

            if(t_kilo<self.eve_kilo):
                if(min(uzaklıklar)==self.eve_1_konum):
                    self.eve_1_hareket="Geliyor"
                    time.sleep(1)
                    print("1.Asansör :",self.eve_1_hareket)
                    time.sleep(1)
                    self.eve_1_hareket="Aşağıya İniyor"
                    print("1.Asansör :",self.eve_1_hareket)
                elif(min(uzaklıklar)==self.eve_2_konum):
                    self.eve_2_hareket="Geliyor"
                    time.sleep(1)
                    print("2.Asansör :",self.eve_2_hareket)
                    time.sleep(1)
                    self.eve_2_hareket="Aşağıya İniyor"
                    print("2.Asansör :",self.eve_2_konum)
                elif(min(uzaklıklar)==self.eve_3_konum):
                    self.eve_3_hareket="Geliyor"
                    time.sleep(1)
                    print("3.Asansör :",self.eve_3_hareket)
                    self.eve_3_hareket="Aşağıya İniyor"
                    print("3.Asansör :",self.eve_3_hareket)
            elif(t_kilo>self.eve_kilo):
                if(min(uzaklıklar)==self.eve_1_konum):
                    self.eve_1_konum="Duruyor"
                    print("1.Asansör :",self.eve_1_konum)
                elif(min(uzaklıklar)==self.eve_2_konum):
                    self.eve_2_konum="Duruyor"
                    print("2.Asansör :",self.eve_2_konum)
                elif(min(uzaklıklar)==self.eve_3_konum):
                    self.eve_3_konum="Duruyor"
                    print("3.Asansör :",self.eve_3_konum)

            button_3=input("Push Button")
            if(button_3 == ">"):
                user_3=int(input("Kilonuzu Giriniz :"))
                if(self.eve_1_hareket=="Duruyor" or "Duruyor"==self.eve_2_hareket or "Duruyor"==self.eve_3_hareket):
                    uzaklıklar.remove(min(uzaklıklar))
                    if(min(uzaklıklar)==self.eve_1_konum):
                        self.eve_1_hareket="Geliyor"
                        print("1.Asansör :",self.eve_1_hareket)
                        if(user_3>self.eve_kilo):
                            self.eve_1_hareket="Duruyor"
                            print("1.Asansör :",self.eve_1_hareket)
                        else:
                            self.eve_1_hareket="Yukarıya Çıkıyor"
                            print("1.Asansör :",self.eve_1_hareket)
                    elif(min(uzaklıklar)==self.eve_2_konum):
                        self.eve_2_hareket="Geliyor"
                        print("2.Asansör :",self.eve_2_hareket)
                        if(user_3>self.eve_kilo):
                            self.eve_2_hareket="Duruyor"
                            print("2.Asansör :",self.eve_2_hareket)
                        else:
                            self.eve_2_hareket="Yukarıya Çıkıyor"
                            print("2.Asansör :",self.eve_2_hareket)
                    elif(min(uzaklıklar)==self.eve_3_konum):
                        self.eve_2_hareket="Geliyor"
                        print("3.Asansör :",self.eve_3_hareket)
                        if(user_3>self.eve_kilo):
                            self.eve_3_hareket="Duruyor"
                            print("3.Asansör :",self.eve_3_hareket)
                        else:
                            self.eve_3_hareket="Yukarıya Çıkıyor"
                            print("3.Asansör :",self.eve_3_hareket)
        elif((button==">" and button_1=="<") or (button=="<" and button_1==">")):

            katlar=[self.eve_1_konum,self.eve_2_konum,self.eve_3_konum]
            uzaklıklar=[]
            for i in katlar:
                a=i
                uzaklıklar.append(a)
            if(button==">" and button_1=="<"):
                uzaklıklar.sort()
                kat=uzaklıklar[0]
                kat_1=uzaklıklar[1]
                kat_2=uzaklıklar[2]

                if(button==">"):
                    if(kat==self.eve_1_konum):
                        self.eve_1_hareket="Geliyor"
                        time.sleep(1)
                        user=int(input("Kilonuzu Giriniz :"))
                        user_1=int(input("Kilonuzu Giriniz :"))
                        t_kilo=user+user_1
                        if(t_kilo>self.eve_kilo):
                            self.eve_1_hareket="Duruyor"
                            print("1.Asansor :",self.eve_1_hareket)
                        elif(t_kilo<self.eve_kilo):
                            self.eve_1_hareket="Yukarıya Çıkıyor"
                            print("1.Asansor :",self.eve_1_hareket)
                    elif(kat==self.eve_2_konum):
                        self.eve_2_hareket="Geliyor"
                        time.sleep(1)
                        user=int(input("Kilonuzu Giriniz :"))
                        user_1=int(input("Kilonuzu Giriniz :"))
                        t_kilo=user+user_1
                        if(t_kilo>self.eve_kilo):
                            self.eve_2_hareket="Duruyor"
                            print("2.Asansor :",self.eve_2_hareket)
                        elif(t_kilo<self.eve_kilo):
                            self.eve_2_hareket="Yukarıya Çıkıyor"
                            print("2.Asansor :",self.eve_2_hareket)
                    elif(kat==self.eve_3_konum):
                        self.eve_3_hareket="Geliyor"
                        time.sleep(1)
                        user=int(input("Kilonuzu Giriniz :"))
                        user_1=int(input("Kilonuzu Giriniz :"))
                        t_kilo=user+user_1
                        if(t_kilo>self.eve_kilo):
                            self.eve_3_hareket="Duruyor"
                            print("3.Asansor :",self.eve_3_hareket)
                        elif(t_kilo<self.eve_kilo):
                            self.eve_3_hareket="Yukarıya Çıkıyor"
                            print("3.Asansor :",self.eve_3_hareket)
                if(button_1=="<"):
                                if(kat_1==self.eve_1_konum):
                                    self.eve_1_hareket="Geliyor"
                                    time.sleep(1)
                                    user=int(input("Kilonuzu Giriniz :"))
                                    user_1=int(input("Kilonuzu Giriniz :"))
                                    t_kilo=user+user_1
                                    if(t_kilo>self.eve_kilo):
                                        self.eve_1_hareket="Duruyor"
                                        print("1.Asansor :",self.eve_1_hareket)
                                    elif(t_kilo<self.eve_kilo):
                                        self.eve_1_hareket="Aşağıya İniyor"
                                        print("1.Asansor :",self.eve_1_hareket)
                                elif(kat_1==self.eve_2_konum):
                                    self.eve_2_hareket="Geliyor"
                                    time.sleep(1)
                                    user=int(input("Kilonuzu Giriniz :"))
                                    user_1=int(input("Kilonuzu Giriniz :"))
                                    t_kilo=user+user_1
                                    if(t_kilo>self.eve_kilo):
                                        self.eve_2_hareket="Duruyor"
                                        print("2.Asansor :",self.eve_2_hareket)
                                    elif(t_kilo<self.eve_kilo):
                                        self.eve_2_hareket="Aşağıya İniyor"
                                        print("2.Asansor :",self.eve_2_hareket)
                                elif(kat_1==self.eve_3_konum):
                                        self.eve_3_hareket="Geliyor"
                                        time.sleep(1)
                                        user=int(input("Kilonuzu Giriniz :"))
                                        user_1=int(input("Kilonuzu Giriniz :"))
                                        t_kilo=user+user_1
                                        if(t_kilo>self.eve_kilo):
                                            self.eve_3_hareket="Duruyor"
                                            print("3.Asansor :",self.eve_3_hareket)
                                        elif(t_kilo<self.eve_kilo):
                                            self.eve_3_hareket="Aşağıya İniyor"
                                            print("3.Asansor :",self.eve_3_hareket)
            elif(button=="<" and button_1==">"):
                uzaklıklar.sort()
                kat=uzaklıklar[0]
                kat_1=uzaklıklar[1]
                kat_2=uzaklıklar[2]

                if(button=="<"):
                    if(kat==self.eve_1_konum):
                        self.eve_1_hareket="Geliyor"
                        time.sleep(1)
                        user=int(input("Kilonuzu Giriniz :"))
                        user_1=int(input("Kilonuzu Giriniz :"))
                        t_kilo=user+user_1
                        if(t_kilo>self.eve_kilo):
                            self.eve_1_hareket="Duruyor"
                            print("1.Asansor :",self.eve_1_hareket)
                            uzaklıklar.remove(kat)
                            print(uzaklıklar)
                        elif(t_kilo<self.eve_kilo):
                            self.eve_1_hareket="Aşağıya İniyor"
                            print("1.Asansor :",self.eve_1_hareket)

                    elif(kat==self.eve_2_konum):
                        self.eve_2_hareket="Geliyor"
                        time.sleep(1)
                        user=int(input("Kilonuzu Giriniz :"))
                        user_1=int(input("Kilonuzu Giriniz :"))
                        t_kilo=user+user_1
                        if(t_kilo>self.eve_kilo):
                            self.eve_2_hareket="Duruyor"
                            print("2.Asansor :",self.eve_2_hareket)

                        elif(t_kilo<self.eve_kilo):
                            self.eve_2_hareket="Aşağıya İniyor"
                            print("2.Asansor :",self.eve_2_hareket)

                    elif(kat==self.eve_3_konum):
                        self.eve_3_hareket="Geliyor"
                        time.sleep(1)
                        user=int(input("Kilonuzu Giriniz :"))
                        user_1=int(input("Kilonuzu Giriniz :"))
                        t_kilo=user+user_1
                        if(t_kilo>self.eve_kilo):
                            self.eve_3_hareket="Duruyor"
                            print("3.Asansor :",self.eve_3_hareket)

                        elif(t_kilo<self.eve_kilo):
                            self.eve_3_hareket="Aşağıya İniyor"
                            print("3.Asansor :",self.eve_3_hareket)
                    if(button_1==">"):
                                if(kat_1==self.eve_1_konum):
                                    self.eve_1_hareket="Geliyor"
                                    time.sleep(1)
                                    user=int(input("Kilonuzu Giriniz :"))
                                    user_1=int(input("Kilonuzu Giriniz :"))
                                    t_kilo=user+user_1
                                    if(t_kilo>self.eve_kilo):
                                        self.eve_1_hareket="Duruyor"
                                        print("1.Asansor :",self.eve_1_hareket)
                                        uzaklıklar.remove(kat)
                                        print(uzaklıklar)
                                    elif(t_kilo<self.eve_kilo):
                                        self.eve_1_hareket="Yukarıya Çıkıyor"
                                        print("1.Asansor :",self.eve_1_hareket)

                                elif(kat_1==self.eve_2_konum):
                                        self.eve_2_hareket="Geliyor"
                                        time.sleep(1)
                                        user=int(input("Kilonuzu Giriniz :"))
                                        user_1=int(input("Kilonuzu Giriniz :"))
                                        t_kilo=user+user_1
                                        if(t_kilo>self.eve_kilo):
                                            self.eve_2_hareket="Duruyor"
                                            print("2.Asansor :",self.eve_2_hareket)

                                        elif(t_kilo<self.eve_kilo):
                                            self.eve_2_hareket="Yukarıya Çıkıyor"
                                            print("2.Asansor :",self.eve_2_hareket)

                                elif(kat_1==self.eve_3_konum):
                                    self.eve_3_hareket="Geliyor"
                                    time.sleep(1)
                                    user=int(input("Kilonuzu Giriniz :"))
                                    user_1=int(input("Kilonuzu Giriniz :"))
                                    t_kilo=user+user_1
                                    if(t_kilo>self.eve_kilo):
                                        self.eve_3_hareket="Duruyor"
                                        print("3.Asansor :",self.eve_3_hareket)

                                    elif(t_kilo<self.eve_kilo):
                                        self.eve_3_hareket="Yukarıya Çıkıyor"
                                        print("3.Asansor :",self.eve_3_hareket)


while True:

    eve=asansor()

    print("""******************************

        İŞLEMLER.......
        
        1-Asansör Çağır

*******************************""")

    işlem=input("İşlem Seçiniz :")

    if(işlem=="1"):
        eve.hareket()

