N1 = N2 = None


def suma(a, b):
    return a + b


def resta(a, b):
    return a - b


def producto(a, b):
    return a * b


def division(a, b):
    return a / b


def reset_calculator():
    global N1, N2
    N1 = float(input("Introduce tu primer número: "))
    N2 = float(input("Introduce tu segundo número: "))


def print_calculator_header():
    print("""
    Menu de opción Morales, Morales, Velasco:
    1) Sumar los dos números
    2) Restar los dos números
    3) Multiplicar los dos números
    4) Dividir los dos números
    5) Cambiar los números elegidos
    6) Apagar calculadora
    """)


def calculator():
    global N1, N2
    while True:
        opcion = int(input("\nElige una opción: "))

        if opcion == 1:
            print("RESULTADO: La suma de {} + {}, es igual {}".format(N1, N2, suma(N1, N2)))
        elif opcion == 2:
            print("RESULTADO: La resta de {} - {}, es igual {}".format(N1, N2, resta(N1, N2)))
        elif opcion == 3:
            print("RESULTADO: El producto de {} * {}, es igual {}".format(N1, N2, producto(N1, N2)))
        elif opcion == 4:
            print("RESULTADO: El producto de {} / {}, es igual {}".format(N1, N2, division(N1, N2)))
        elif opcion == 5:
            reset_calculator()
        elif opcion == 6:
            break
        else:
            print("Opción incorrecta, intenta de nuevo")


if __name__ == "__main__":
    reset_calculator()
    print_calculator_header()
    calculator()
