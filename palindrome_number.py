for i in range (100,1000):
    j=i
    a=(i*j)
    b=str(a)
   # print("normal sayı",str(a))
   # print("ters sayı",b[::-1])
    if(b[::-1]==str(a)):
        print(a)
        print("i:",i)
        print("j",j)




