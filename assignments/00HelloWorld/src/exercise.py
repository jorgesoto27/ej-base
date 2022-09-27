def main():
    #escribe tu código abajo de esta línea
    n = int(input())
    lista1 = []
    for i in range (n):
        x = int(input())
        lista1.append(x)
    lista2 = []
    for i in range (0, len(lista1)):
        y = lista1 [i]**2
        lista2.append(y)

    print(f"{lista1}")
    print(f"{lista2}")

if __name__=='__main__':
    main()
