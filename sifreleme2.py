def Sifrele(metin, Anahtar): #sifrele adında fonksiyon oluşturdum içine metin ve Anahtar parametreleri girdim.
    Sifreli_Metin = ''

    Alfabe = [
        'a', 'b', 'c', 'ç' , 'd', 'e', 'f', 'g', 'ğ' , 'h', 'ı' , 'i', 'j', 'k', 'l', 'm',
        'n', 'o', 'ö' , 'p', 'r', 's', 'ş', 't', 'u', 'ü' , 'v', 'y', 'z'
    ]   #Türkçe harfleri alfabeyi tanımladım
    for i in metin: #for döngüsü kurdum.

        if i not in Alfabe:  #if ile eğer yoksa 1 artır dedim
            Sifreli_Metin += i
        else: #Anahtar alfabe değişkenlerini kullanarak uzunluk alma işlemlerini kullandım.
            Sifreli_Metin += Alfabe[
                (Alfabe.index(i) + Anahtar) % len(Alfabe)]

    print("Şifrelenmiş Metin:", Sifreli_Metin)


Anahtar = int(7) #anahtarı 7 olarak belirledim girilen metin harflerini 7 ofset öteleyecek.

Metin = input("Cümle Yazın: ") #kullanıcıdan veri aldım.
Sifrele(Metin, Anahtar) #fonksiyon parametrelerini çağırdım.


