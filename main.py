def SezarSifrele(Metin, HarfAtla): #SezarSifrele adında fonksiyon tanımlayıp içine Metin ve HarfAtla parametrelerini girdim.
    sifreleme = "" #sifreleme adında veri gelecek boş string tanımladım.
    for i in Metin: #for döngüsü ile metin içinde dönmesini sağladım.
        sifreleme = sifreleme + chr(ord(i) + HarfAtla) #ascii kodu kullanarak metnin şifrelenme işlemini gerçekleştirdim.
    print("Şifrelenmiş Cümle:", sifreleme) #ekrana yazdırma.


print("METNİ ŞİFRELEME")

Cümle = input("Şifrelenecek bir cümle yazın:") #Kullanıcıdan şifrelenecek cümleyi aldım.
x = input("Anahtar:") #Şifrelenecek kelimenin kaç harf öteleneceğini belirlemek için anahtar tanımladım ve bunuda kullanıcıya bıraktım.

SezarSifrele(Cümle, int(x))

print("-----------------------------------------------------")
print("ŞİFRELİ METNİ ÇÖZME.")
sifresiz=input("Şifreli Metni Giriniz:") #Şifreli metni çözmek için kullanıcıdan veri aldım.
def sifrele(metin): #sifrele adında fonksiyon oluşturdum ve içine metin parametresi girdim.
    sifrelimetin=""
    for harf in metin: #for döngüsü ile harflerin metin içinde dönmesini sağladım.
        asciikod=ord(harf)  #ascii işlemleri.
        asciikod=asciikod-int(x)
        karakterkod=chr(asciikod)
        sifrelimetin=sifrelimetin+karakterkod
    print("Şifresiz:",metin,"Şifreli:",sifrelimetin)  #ekrana yazıdrdım.

sifrele(sifresiz)