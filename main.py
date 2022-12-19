from PIL import Image
import random
import time
list = ["taş","kağıt","makas"]
sevinc = ["kolaysın","ez","öğrende gel","bb canısı"]
uzuntu = ["önümüzdeki maçlara bakıcaz","sonraki sefere","hile var","şike yapma"]
print("sadece 'taş/kağıt/makas' yazın (resmi kapatmadan bir sonraki döngü başlamaz)")
while True:
    m = int(input("kaça kadar saymamı istersin :"))
    for i in range(0,m):
        print(i+1,end=" ")
        time.sleep(1)
    x = random.randint(0,len(list)-1)
    print("")
    deger = list[x]
    if deger == "taş":
        ımage = Image.open(r"C:\Users\bugra\OneDrive\Masaüstü\oyun\rock.jpg")
        ımage.show()
    elif deger == "kağıt":
        ımage = Image.open(r"C:\Users\bugra\OneDrive\Masaüstü\oyun\paper.jpg")
        ımage.show()
    elif deger == "makas":
        ımage = Image.open(r"C:\Users\bugra\OneDrive\Masaüstü\oyun\makas.jpg")
        ımage.show()
    else:
        print("doğru değer girmedin")
    #mesaj yazdır
    n = input("yaptığın sonucu söyle hile yapma :)     :")
    o = random.randint(0,len(sevinc)-1)
    if n == "taş" and deger == "makas":     #yenilgi
        print(uzuntu[o])
    elif n == "taş" and deger == "kağıt":
        print(sevinc[o])
    elif n == "makas" and deger == "kağıt":
        print(uzuntu[o])
    elif n == "makas" and deger == "taş":
        print(sevinc[o])
    elif n == "kağıt" and deger == "makas":
        print(sevinc[o])
    elif n == "kağıt" and deger == "taş":
        print(uzuntu[o])
    elif n != "taş" or n != "kağıt" or n != "makas":
        print("düzgün değer girmedin üzme beni bro :( \nbiraz kendimi toplamam lazım bi 5 sn kadar bekle")
        time.sleep(5)
        print("geldim devamke ...")
        continue
    else:
        print("berabere")
    #bir oyun daha
    x = input("bir oyun daha ??? :(e/h):").lower()
    if x == "e":
        continue
    elif x == "h":
        break
    else:
        print("girilen değer hatalı evet olarak anladım seni ...")