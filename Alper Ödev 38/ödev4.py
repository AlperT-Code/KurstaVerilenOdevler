def kare_ciz(kenar, sembol, dolu):
    for i in range(kenar):
        if dolu or i == 0 or i == kenar - 1:
            print(sembol * kenar)
        else:  
            print(sembol + " " * (kenar - 2) + sembol if kenar > 1 else sembol)


kare_ciz(5, '*', True)  
print()
kare_ciz(5, '*', False)  

#chatgpt yardım etti