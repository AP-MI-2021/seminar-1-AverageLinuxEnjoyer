def inverse(x: int) -> bool:
    '''
    Functie care returneaza un intreg cu cifrele in ordine inversa.
    
    x - intregul dat ca parametru
    '''
    y: int = 0

    while x:
        y *= 10
        y += x % 10
        x //= 10


    return y

assert inverse(234) == 432
assert inverse(101) == 101
assert inverse(45678) == 87654