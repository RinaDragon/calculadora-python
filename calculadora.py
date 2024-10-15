def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "No se puede dividir entre 0"

def menu():
    print("Selecciona una operación:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")

    opcion = input("Introduce tu opción (1/2/3/4): ")
    return opcion

def main():
    while True:
        opcion = menu()

        if opcion in ['1', '2', '3', '4']:
            num1 = float(input("Introduce el primer número: "))
            num2 = float(input("Introduce el segundo número: "))

            if opcion == '1':
                print(f"La suma es: {sumar(num1, num2)}")
            elif opcion == '2':
                print(f"La resta es: {restar(num1, num2)}")
            elif opcion == '3':
                print(f"La multiplicación es: {multiplicar(num1, num2)}")
            elif opcion == '4':
                print(f"La división es: {dividir(num1, num2)}")
        else:
            print("Opción no válida.")

        continuar = input("¿Quieres realizar otra operación? (s/n): ")
        if continuar.lower() != 's':
            break

if __name__ == "__main__":
    main()