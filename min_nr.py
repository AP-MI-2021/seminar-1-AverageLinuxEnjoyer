def min(x: int, y: int, z: int) -> int:
    '''
    Functie care returneaza minimul a 3 intregi.
    
    x, y, z - intregii a caror minim va fi returnat.
    '''
    if x < y and x < z:
        return x
    elif y < x and y < z:
        return y
    else:
        return z

assert min(1,2,3) == 1
assert min(4,4,4) == 4
assert min(-3,2,7) == -3
assert min(0,2234434634663,-3243) == -3243
