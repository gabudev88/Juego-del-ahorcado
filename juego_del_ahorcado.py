## JUEGO DEL AHORCADO
## TIENES 5 OPORTUNIDADES PARA ACERTAR CADA LETRA DE LA PALABRA

## INGRESO UNA PALABRA
palabra = input("Ingresa una palabra: ")

## CADA LETRA DE DICHA PALABRA ES CONVERTIDA EN UN ELEMENTO DE LA SIGUIENTE LISTA 
lista_palabra = []

def palabra_ingresada(palabra):
    
    for n in palabra:
        lista_palabra.append(n)

    return lista_palabra

palabra_ingresada(palabra)

## CREAMOS UNA LISTA VACIA PARA QUE NOS SIRVA DE GUIA AL JUGADOR

lista_vacia = []

def cantidad_de_palabras(lista):
    for n in lista:
        lista_vacia.append("_")
    
    print(f"La palabra es la siguiente: {lista_vacia}")

cantidad_de_palabras(lista_palabra)

## DESARROLLO DEL JUEGO
## DECLARAMOS VARIABLES

intentos = 1

## EL SIGUIENTE STRING SE COMPLETA CON LOS ELEMENTOS DE LA LISTA DE LA PALABRA INGRESADA 
string_palabra = ""
for n in lista_palabra:
    string_palabra += n

## ESTE STRING SE VA COMPLETANDO A MEDIDA QUE ACIERTE CADA LETRA Y LO COMPARA CON LA PALABRA INGRESADA
string_vacia = ""

while (intentos<5):
    vuelta_letra = 1
    letra = input("Ingrese una letra: ")
    
    for n in lista_palabra:
        if n == letra:
            acierto = lista_palabra.index(n)
            lista_vacia.pop(acierto)
            lista_vacia.insert(acierto, n)
            string_vacia += n
        else:
            vuelta_letra = vuelta_letra + 1
            if vuelta_letra > len(lista_palabra):
              intentos = intentos + 1
              print("Usted tiene solo 5 intentos")
              print(f"Numero de intentos: {intentos}")
              if intentos == 5:
                print("Fin del juego: Mejor suerte para la proxima!")
              else:
                pass

    print(lista_vacia)

    if string_palabra==string_vacia:
        print("Fin del juego: Felicitaciones!")
        intentos = 5
    else:
        pass

