from math import prod

def carpim_hesapla(liste):
    return prod(liste)

def min_bul(liste):
    return min(liste)

def asal_sayi_sayisi(liste):
    def asal_mi(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    return sum(1 for num in liste if asal_mi(num))

def eleman_kaldir(liste, sayi):
    eski_uzunluk = len(liste)
    liste[:] = [x for x in liste if x != sayi]
    return eski_uzunluk - len(liste)

def iki_liste_birlestir(liste1, liste2):
    return liste1 + liste2

def elemanlari_ussu(liste, us):
    return [x ** us for x in liste]


dizi = [2, 3, 5, 7, 8, 10]
print("Çarpım:", carpim_hesapla(dizi))
print("Minimum:", min_bul(dizi))
print("Asal Sayı Sayısı:", asal_sayi_sayisi(dizi))
print("Eleman kaldırıldı:", eleman_kaldir(dizi, 5), "Yeni Liste:", dizi)
print("Birleşmiş Liste:", iki_liste_birlestir([1, 2, 3], [4, 5, 6]))
print("Üs Alınmış Liste:", elemanlari_ussu([2, 3, 4], 3))