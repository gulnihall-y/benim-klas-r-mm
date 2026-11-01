
#1.görev
ad = input("Adınızı giriniz: ")
soyad = input("Soyadınızı giriniz:")
şehir = input("Yaşadığınız şehri giriniz:")

print(f"Merhaba {şehir}'li {ad} {soyad}.Tanıştığıma memnun oldum.")


#2.görev
def indirim_hesapla(fiyat, indirim_oranı):
    indirim_tutarı = fiyat * (indirim_oranı/100)
    son_fiyat = fiyat - indirim_tutarı
    return indirim_tutarı, son_fiyat 

girilen_fiyat = float (input("Ürünün fiyatı giriniz.(TL):"))
girilen_oran = float(input("İndirim yüzdesini giriniz.:"))

hesaplanan_indirim, yeni_fiyat = indirim_hesapla(girilen_fiyat, girilen_oran)

print(f"İndirim Tutarı: {hesaplanan_indirim} TL")
print(f"İndirimli Son Fiyat: {yeni_fiyat} TL")


#3.görev
def ehliyet_kontrolü(yas):
    if  yas >= 18:
        return "Ehliyet alabilirsin!"
    else :
        return "Ehliyet alabilmek için henüz yaşınız tutmuyor."
kullanıcı_yaşı = float(input("Lütfen yaşınızı giriniz.:")) 

sonuc = ehliyet_kontrolü(kullanıcı_yaşı)
print(sonuc)


#4.görev
def harf_notu_hesapla(vize,final):
 ortalama = (vize*0.4) + (final*0.6)

 if ortalama >= 85:
     harf= "AA"
 elif ortalama >=70:
     harf= "BB"
 elif ortalama >= 50:
     harf= "CC"
 else :
     harf= "FF"
     
 return ortalama, harf
girilen_vize = float(input("Vize notunuzu giriniz.:"))
girilen_final = float(input("Final notunuzu giriniz.:"))

ders_ortalaması , harf_notu = harf_notu_hesapla(girilen_vize ,girilen_final)

print(f"Dönem Ortalamanız: {ders_ortalaması}")
print(f"Harf Notunuz: {harf_notu}")
