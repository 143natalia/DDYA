def main():
    num = int(input("Ingrese un número y te dire algunas de sus caracteristicas: "))

    if num > 0:
        print("El número es positivo. ")
    if num == 0:
        print("El número es cero.\nEl número hace parte de la sucesión de fibonacci.")
    if num <0:
        print("El número es negativo. ")
    
    f1 = 1
    f2 = 0
    fibo = f1 + f2

    while fibo <= num:
        f2 = f1
        f1 = fibo
        fibo = f1 + f2
        if fibo == num:
            print("El número hace parte de la sucesión de fibonacci. ")


main()