def isPrime(x: int) -> bool:
    '''
    Functie care verifica daca un intreg e prim si returneaza valoarea bool corespunzatoare.
    
    x - intregul verificat
    '''
    if x < 2:
        return False
    
    for i in range(2, x // 2 + 1):
        if x % i == 0:
            return False

    return True

assert isPrime(1) == False
assert isPrime(2) == True
assert isPrime(4) == False
assert isPrime(36) == False
assert isPrime(0) == False
assert isPrime(17) == True

def arePrimes(n: int) -> None:
    '''
    Functie care citeste n intregi si afiseaza daca sunt sau nu prime.

    n - numarul de intregi
    '''

    for i in range(n):
        nr = int(input("Introdu un intreg:"))
        if isPrime(nr):
            print(f"{nr} e prim.")
        else:
            print(f"{nr} nu e prim.")
