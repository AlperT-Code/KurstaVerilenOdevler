import random

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

#Oyun
def bulls_and_cows(secret, guess, attempt=1):
    if secret == guess:
        print(f"Tebrikler! {attempt}. denemenizde kazandınız.")
        return
    
    bulls = sum(1 for i in range(4) if secret[i] == guess[i])
    cows = sum(1 for digit in set(guess) if digit in secret) - bulls
    
    print(f"{guess}: {bulls} Bulls, {cows} Cows")
    
    new_guess = input("Yeni tahmininizi girin: ")
    bulls_and_cows(secret, new_guess, attempt + 1)

if __name__ == "__main__":
    #EBOB
    a = int(input("Birinci sayıyı girin: "))
    b = int(input("İkinci sayıyı girin: "))
    print(f"EBOB({a}, {b}) = {gcd(a, b)}")
    
    #Oyun
    secret_number = ''.join(random.sample("0123456789", 4))
    print("4 basamaklı bir sayı tahmin edin.")
    user_guess = input("Tahmininizi girin: ")
    bulls_and_cows(secret_number, user_guess)
