def password():
    """
    Ejercicio 10 - Validador de Contraseña

    Leer una contraseña mediante input(). Validar que cumpla con los siguientes requisitos:
    1. Debe tener al menos 8 caracteres de longitud
    2. Debe contener al menos un número (usar el operador in para verificar cada dígito del 0 al 9)

    Si cumple ambos requisitos, imprimir "Contraseña valida".
    Si no cumple, imprimir cuál requisito falta.

    Ejemplo:
        Para la entrada "abc12345", la salida esperada es:
        Contraseña valida

        Para la entrada "abc123", la salida esperada es:
        Contraseña muy corta

        Para la entrada "abcdefgh", la salida esperada es:
        Debe contener un numero

        Para la entrada "abc", la salida esperada es:
        Contraseña muy corta
        Debe contener un numero
    """
    my_password = input()
    longitud = len(my_password)
    num_check = '1' in my_password or '2' in my_password or '3' in my_password or '4' in my_password or '5' in my_password or '6' in my_password or '7' in my_password or '8' in my_password or '9' in my_password or '0' in my_password
    invalid = False

    if longitud < 8:
        print("Contraseña muy corta")
        invalid = True
    if not num_check:
        print("Debe contener un numero")
        invalid = True
    if not invalid:
        print("Contraseña valida")




