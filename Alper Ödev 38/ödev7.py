def palindrom_mu(sayi):
    sayi_str = str(sayi)
    return sayi_str == sayi_str[::-1]  


print(palindrom_mu(123321))  
