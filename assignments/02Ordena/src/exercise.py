def main():
    # Escribe el código adecuado para completar el programa
    x = int(input("Ingresa el primer número: "))
    y = int(input("Ingresa el segundo número: "))
    z = int(input("Ingresa el tercer número: "))
    
    if x>y:
        if y>z:
            print (x)
            print(y)
            print (z)
        elif x>z:
            print(x)
            print(z)
            print(y)
    elif x>z:
        print(y)
        print(x)
        print(z)
    elif z>y:
        print(z)
        print(y)
        print(x)
    else:
        print(y)
        print(z)
        print(x)
        


if __name__=='__main__':
    main()
