def leap_year():
    """
    Ejercicio 11 (Desafío) - Año Bisiesto

    Leer un año mediante input(). Determinar si es un año bisiesto e imprimir el resultado.
    Un año es bisiesto si:
    - Es divisible por 4, Y
    - NO es divisible por 100, O es divisible por 400

    Ejemplo:
        Para la entrada "2000", la salida esperada es:
        El año 2000 es bisiesto

        Para la entrada "2001", la salida esperada es:
        El año 2001 no es bisiesto

        Para la entrada "1700", la salida esperada es:
        El año 1700 no es bisiesto
    """
    anio = int(input())
    cond_a = anio % 4 == 0
    cond_b = anio % 100 == 0
    cond_c = anio % 400 == 0

    if cond_a and (not cond_b or cond_c):
        print(f"El año {anio} es bisiesto")
    else:
        print(f"El año {anio} no es bisiesto")

