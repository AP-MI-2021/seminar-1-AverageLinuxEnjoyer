from min_nr import min as myMin
from inverse_nr import inverse as myInverse
from prime_nr import isPrime
from prime_nr import arePrimes

def main():
    option = '?'
    while True:
        print("Ce functionalitate vrei sa foloseti?")
        print("(1) - determinarea minimului a trei numere")
        print("(2) - verificarea unui numar daca e prim")
        print("(3) - verificarea unei serii de numere daca sunt prime")
        print("(4) - determinarea inversului unui numar")
        print("(x) - iesire program")
        option = input()

        if option == '1':
            x = int(input("Introdu primul numar:"))
            y = int(input("Introdu al doilea numar:"))
            z = int(input("Introdu al treilea numar:"))
            print(f"Minimul celor trei numere e {myMin(x,y,z)}")
        elif option == '2':
            x = int(input("Introdu numarul:"))
            if isPrime(x):
                print(f"{x} e prim")
            else:
                print(f"{x} nu e prim")
        elif option == '3':
            n = int(input("Cate numere vrei sa verifici?"))
            arePrimes(n)
        elif option == '4':
            x = int(input("Introdu numarul:"))
            print(f"Inversul lui {x} e {myInverse(x)}")
        else:
            break

if __name__ == "__main__":
    main()


