import math

print("""
*********************************
1-Toplama İşlemi
2-Çıkarma İşlemi
3-Çarpma İşlemi
4-Bölme İşlemi
5-Karekök hesaplama
6-Üst Alma
7-Cos Hesaplama
8-Sin hesaplama

**********************************
""")
while True:
    i=int(input("İşlem Seçiniz:"))
    a=float(input("1.Sayı Giriniz:"))
    b=float(input("2.Sayı Giriniz:"))

    if(i==1):
        print(a+b)

    elif(i==2):
        print(a-b)
    elif(i==3):
        print(a*b)
    elif(i==4):
        print(a/b)
    elif(i==5):
        toplama=math.sqrt(a)
        toplama1=math.sqrt(b)
        print("Birinci Sayı Kök:",toplama,"\nİkinci Sayı Kök:",toplama1)
    elif(i==6):
        ust=math.pow(a,b)
        print("Birinci Sayı Üstü İkinci Sayı :",ust)

    elif(i==7):
        cos1=math.cos(a)
        cos2=math.cos(b)
        print("Birinci Sayı Cos:",cos1,"\nİkinci Sayı Cos:",cos2)
    elif(i==8):
        sin1=math.sin(a)
        sin2=math.sin(b)
        print("Birinci Sayı Cos:",sin1,"\nİkinci Sayı Cos:",sin2)





