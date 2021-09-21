def hatalar(sayı):
    if(sayı%2!=0):
        raise ValueError("Tek sayı Girmeyiniz")
    else:
        print("Sayı Çifttir.")

try:
    print(hatalar(13))
except ValueError:
    print("Fonksiyon Hata Verdi.")
