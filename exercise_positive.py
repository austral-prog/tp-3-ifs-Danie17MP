def positive():
    """
    Ejercicio 1 - Clasificar Número

    Leer un número entero mediante input(). Determinar si es positivo, negativo o cero
    e imprimir el resultado correspondiente.

    Ejemplo:
        Para la entrada "5", la salida esperada es:
        El numero es positivo

        Para la entrada "-3", la salida esperada es:
        El numero es negativo

        Para la entrada "0", la salida esperada es:
        El numero es cero
    """
    number = int(input("Ingrese numero: "))
    if number < 0:
        print("El numero es negativo")
    elif number > 0:
        print("El numero es positivo")
    else:
        print("El numero es cero")

#positive()