def çift_sayılar(sayi1, sayi2):
    sayii1 = max(sayi1, sayi2)
    sayii2 = min(sayi1, sayi2)
    for i in range(sayii1,sayii2 + 1):
        if i % 2 == 0:
            print(i , end="")
çift_sayılar(3,15)            
