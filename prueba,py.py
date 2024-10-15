import random

def adivina_el_numero():
    numero_secreto = random.randint(1, 100)
    intentos = 0
    adivinado = False

    print("¡Bienvenido al juego de Adivina el Número!")
    print("He elegido un número entre 1 y 100. ¡Intenta adivinarlo!")

    while not adivinado:
        try:
            intento = int(input("Ingresa tu número: "))
            intentos += 1
            
            if intento < 1 or intento > 100:
                print("Por favor, elige un número entre 1 y 100.")
            elif intento < numero_secreto:
                print("Demasiado bajo. Intenta de nuevo.")
            elif intento > numero_secreto:
                print("Demasiado alto. Intenta de nuevo.")
            else:
                adivinado = True
                print(f"¡Felicidades! Has adivinado el número {numero_secreto} en {intentos} intentos.")
        except ValueError:
            print("Por favor, ingresa un número válido.")

if __name__ == "__main__":
    adivina_el_numero()