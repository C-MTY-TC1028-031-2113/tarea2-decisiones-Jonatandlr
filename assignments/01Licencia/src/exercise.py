
def main():
    edad=int(input("Ingresa tu edad: "))
        
    if edad>0 and edad>=18:
        lic=input("¿Tienes identificación oficial? (s/n):")
        
        if lic=="s":
            print ("Trámite de licencia concedido")
        elif lic=="n":
            print("No cumples requisitos")
        else:
            print("Respuesta incorrecta")
    else:
        print("No cumples requisitos")
        

if __name__ == '__main__':
    main()
