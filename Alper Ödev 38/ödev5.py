def aralik(alt_sinir, ust_sinir):
    if alt_sinir > ust_sinir:
        alt_sinir, ust_sinir = ust_sinir, alt_sinir
    carpim = 1
    for i in range(alt_sinir, ust_sinir + 1):
        carpim *= i
    return carpim
print(aralik(5, 8))  
print(aralik(10, 7))  
