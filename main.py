import random 
def adivina_el_numero():
    numero_secreto = random.randint(1, 10)
    intentos = 0
    adivinado = False
    
    print("Bienvenido al juego de adivinanza de numeros")
    print("Estoy pensando en un numero entre 1 y 10")
    
    while not adivinado:
        intento = int(input("Adivina el numero: "))
        intentos += 1
        
        if intento < numero_secreto:
            print("Demasiado bajo, intenta de nuevo. ")
        elif intento > numero_secreto:
            print("Demasiado alto, intenta de nuevo. ")
        else:
            adivinado = True
            print("Felicidades, adivinaste el numero en {intentos} intentos. ")

adivina_el_numero()