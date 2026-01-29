a = input("İlk sayıyı girin: ")
sayi_1 = int(a)
b = input("İkinci sayıyı girin: ")
sayi_2 = int(b)
print("Toplama için 1, çıkarma için 2, çarpma için, 3, bölme için 4, üssü almak için 5 tuşuna basın.")
print("Ayrıca 6'ya basarak bölmeyi tam sayıya çevirebilir veya 7'ye basarak sayıların modunu alabilirsiniz.")
islem = input("İşlem seçiminizi yapın: ")
if islem == "1":
    print("Sonuç:", sayi_1+sayi_2)
elif islem == "2":
    print("Sonuç:", sayi_1-sayi_2)
elif islem == "3":
    print("Sonuç:", sayi_1*sayi_2)
elif islem == "4":
    print("Sonuç:", sayi_1/sayi_2)
elif islem == "5":
    print("Sonuç:", sayi_1**sayi_2)
elif islem == "6":
    print("Sonuç:", sayi_1//sayi_2)
elif islem == "7":
    print("Sonuç:", sayi_1 % sayi_2)
else:
    print("Uygun seçim yapmadınız.")
