a=input("Lütfen Sayı giriniz: ")
sayılar=list(a)
print("Sayı:",sayılar)
print("Sayı Karakter Uzunluğu :",int(len(sayılar)))
toplam=0

while(True):
    while(True):
        for i in sayılar:
            k=int(i)
            c=(k**int(len(sayılar)))
            toplam +=c
            str(toplam)

        if(toplam==int(a)):
            print("Toplam:",toplam)
            print("Armstong Sayısıdır")
            break
        else:
            print("Toplam:",toplam)
            print("Armstong Sayısı Değildir.")
            break




