import random

def guess_the_number():
    while True:  # Bucle para reiniciar el juego
        secret_number = random.randint(1, 100)
        attemps = 0
        guessed = False

        print("¡Bienvenido al juego de adivinanza de números!")
        print("Estoy pensando en un número entre 1 y 100.")

        while not guessed:
            try:
                attemp = int(input("Adivina el número: "))
                attemps += 1

                if attemp < secret_number:
                    print("Demasiado bajo. Intenta de nuevo.")
                elif attemp > secret_number:
                    print("Demasiado alto. Intenta de nuevo.")
                else:
                    guessed = True
                    print(f"¡Felicidades! Adivinaste el número en {attemps} intentos.")
            except ValueError:
                print("Por favor, ingresa un número válido.")

        # Preguntar al usuario si quiere jugar de nuevo
        play_again = input("¿Quieres jugar de nuevo? (s/n): ").strip().lower()
        if play_again != 's':
            print("Gracias por jugar. ¡Hasta la próxima!")
            break  # Salir del bucle para terminar el programa

# Llamar a la función para iniciar el juego
guess_the_number()


