def main():
    # Escribe tu código abajo de esta línea
    grados= int(input("Introduce los grados: "))

    if 0<=grados<=360:
        if 0<grados<90:
            print("cuadrante 1")
        elif 90<grados<180:
            print("cuadrante 2")
        elif 180<grados<270:
            print("cuadrante 3")
        elif 270<grados<360:
            print("cuadrante 4")
        else:
            print("eje")
    else: 
        print("exede")

if __name__ == '__main__':
    main()
