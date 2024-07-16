import random 
def adivina_el_numero():
    while True:
        numero_secreto = random.randint(1, 10) #genera el numero secreto aleatoriamente
        intentos = 0 #Inicializa el contador de intentos
        adivinado = False #determina si el numero ha sido adivinado
        
        print("Bienvenido al juego de adivinanza de numeros") #Imprime
        print("Estoy pensando en un numero entre 1 y 10") #Imprime
        
        while not adivinado:
            try:
                intento = int(input("Adivina el numero: ")) #Pide que alimine el numero de intentos
                intentos += 1 #Incrementa el numero de intentos
            
                if intento < numero_secreto:
                    print("Demasiado bajo, intenta de nuevo. ")
                elif intento > numero_secreto:
                    print("Demasiado alto, intenta de nuevo. ")
                else:
                    adivinado = True #cambia el estado del numero a encontrado. 
                    print("Felicidades, adivinaste el numero en " + str(intentos) + " intentos.")
            except ValueError:
                print("Ingresa un numero valido, Alcornoque!!")
            
        #Aqui preguntamos si se quiere volver a jugar
        jugar_de_nuevo = input("¿Quieres jugar de nuevo? (s/n): ").strip().lower()
        if jugar_de_nuevo != "s":
            print("Gracias por jugar. ¡Chauu!")
            break  # Salir del bucle para terminar el programa

#Llamamos la funcion para iniciar el juego
adivina_el_numero()

