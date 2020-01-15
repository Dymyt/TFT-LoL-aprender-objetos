from combinaciones import   Combinacion
import random

#Cada objeto del juego en una lista para no equivocarnos al escribir una y otra vez
Objetos = ["espadon", "vara", "arco", "lagrima", "cinturon", "armadura", "capa",
           "guante", "espatula"]

#CREAMOS LOS OBJETOS DE COMBINACION

#Todas las combinaciones de Espadón
Espada_de_la_Muerte = Combinacion("Espada de la muerte", Objetos[0], Objetos[0], "+15 de "
                                                                                 "AD por cada unidad que mate o asista en matar ")
Sable_Pistola = Combinacion("Sable Pistola", Objetos[0], Objetos[1], "Curación del 25% del daño realizado, sin contar objetos")
Asesino_de_Gigantes = Combinacion("Asesino de gigantes", Objetos [0], Objetos [2], "Autoataques hacen un daño adicional del 9%"
                                                                                   " de la vida actual del objetivo")
Shojin = Combinacion("Shojin", Objetos[0], Objetos [3], "Ganas un 18% de tu maná máximo con cada autoataque después de haber realizado"
                                                        " tu ultimate")
Heraldo_Zeke = Combinacion("Heraldo Zeke", Objetos[0], Objetos[4], "Tu y tús aliados en 2 casillas a izq y der ganáis "
                                                                   "20% de velocidad de ataque")
Angel_Guardian = Combinacion("Angel Guardian", Objetos[0], Objetos[5], "Al morir el usuario revive a los dos segundos con "
                                                                       "400 de vida")
Sanguinaria = Combinacion("Sanguinaria", Objetos[0], Objetos[6], "Curación del 40% del daño de tus autoataques")
Filo_Infinito = Combinacion("Filo Infinito", Objetos[0], Objetos[7], "Los ataques críticos pegan un 125% más")

#Todas las combinaciones de Vara grande
Gorro_Rabadon = Combinacion("Gorro Rabadon", Objetos [1], Objetos[1], "Incrementa el poder de habiliad un 75%")
Guinsoo = Combinacion("Guinso", Objetos[1], Objetos[2], "4% de aumento de velocidad de ataque por Autoataque, stackea infinito")
Luden_Echo = Combinacion("Luden Echo", Objetos[1], Objetos[3], "Al usar el ultimate, el objetivo y hasta tres campeones más"
                                                               " situados a max. 2 celdas reciben 120/160/220 de daño mágico"
                                                                " dependiendo del nivel")
Morello = Combinacion("Morello", Objetos[1], Objetos[4], "Los hechizos queman un 18% del hp máximo durante 10 segundos"
                                                         " y aplican heridas graves")
Solaris = Combinacion("Solaris)", Objetos[1], Objetos[5], "Tú y tus aliados en 2 casillas a izq y der ganáis un escudo de"
                                                          " 250/275/300 dependiendo del nivel del campeon que lo tenga equipado")
Ionic_Spark = Combinacion("Ionic Spark", Objetos[1], Objetos [6], "Los enemigos a 3 celdas que casteen su ultimate reciben "
                                                                    "200% de daño mágico de su mana máximo")
Guantelete_AP = Combinacion("Guantelete AP", Objetos[1], Objetos[7], "Las habilidades de ap pueden hacer impactos críticos")

#Todas las combinaciones de Arco de Velocidad
Rapid_FireCannon = Combinacion("Rapid Fire Cannon - Escopeta", Objetos[2], Objetos[2], "Dobla el rango de los ataques")
Statikk_Shiv = Combinacion ("Statick Shiv - Lanza electrica", Objetos [2], Objetos [3], "Cada tercer ataque básico hace"
                                                                                        " 80 de daño mágico y a 2/3/4 enemigos"
                                                                                        " dependiendo del nivel del campeon")
Hydra = Combinacion("Hydra", Objetos[2], Objetos [4], "Ataques Básicos hacen un 3% de daño adicional como daño mágico, e impacta"
                                                      " en los enemigos detras del objetivo adyacentes")
Titans_Resolve = Combinacion("Titans Resolve", Objetos[2], Objetos[5], "Cuando recibes daño o inglinges un impacto crítico consigues"
                                                                        " 2% de daño adicional para el resto del combate hasta 100%. A"
                                                                       " Stacks máximos se gana 25 de armadura y resistencia mágica")
Runaan_Hurricane = Combinacion("Runaan Hurricane", Objetos[2], Objetos[6], "Los ataques básicos impactan a un enemigo adicional con"
                                                                           " una potencia del 60%. Aplica efectos de impacto")
Ultimas_Palabras = Combinacion("Últimas Palabras", Objetos[2], Objetos[7], "Los ataques básicos reducen la armadura del enemigo un"
                                                                           " 90% por 3 segundos")

#Todas las combinaciones de Lágrima
Baston_Arcangel = Combinacion("Vara del arcángel", Objetos[3], Objetos[3], "Después de usar tu ultimate recuperas 20 de mana")
Redencion = Combinacion("Redención", Objetos[3], Objetos [4], "Cuando bajas del 30% de la vida castea un circulo que cura 1200 "
                                                              "de vida despues de 2.5 sec de delay")
Corazon_hielo = Combinacion("Corazón de hielo", Objetos[3], Objetos[5], "Reduce la velocidad de ataque de los enemigos adyacentes"
                                                                        " un 40% por 0,5 segundos")
Hush = Combinacion("Hush", Objetos[3], Objetos[6], "Los ataques básicos tienen un 20% de probabilidad de silenciar a los enemigos"
                                                   " durante 4 segundos")
Guantelete_Mana = Combinacion("Guantelete Mana", Objetos[3], Objetos[7], "Al inicio del turno puedes ganar realizar 50% más de daño"
                                                                         " con habilidades y ataques, o curarte 50 de vida por ataque")

#Todas las combinaciones de Cinturon de Vida
Warmog =  Combinacion("Warmog", Objetos[4], Objetos[4], "Ganar 6% de HP faltante cada segundo, máximo 400hp/s")
Bufo_Rojo = Combinacion("Bufo rojo", Objetos[4], Objetos[5], "Cada AA aplica una quemadura que durante 10s infligirá el 18% de la"
                                                             " vida máxima y reduciendo la curación, no se pueden aplicar 2 cargas")
Zephyr = Combinacion("Zephir", Objetos[4], Objetos[6], "Anula durante 6 segundos al campeon más cercano al lado opuesto del campeón"
                                                       " que lleve equipado este objeto")
Guantelete_Vida = Combinacion("Guantelete Vida", Objetos[4], Objetos[7], "Al inicio de cada ronda ganas un escudo que bloquea el primer"
                                                                         " enemy spell recibido y stunea al enemigo por 4 segundos")

#Todas las combinaciones con Armadura
Malla_Espinas = Combinacion("Malla de Espinas", Objetos[5], Objetos[5], "Niega el daño adicional de impactos criticos, Cuando recibe"
                                                                        " un autoataque hace 80/120/160 de daño magico a los enemigos"
                                                                        " cercanos")
Sword_Breaker = Combinacion("Sword Breaker", Objetos[5], Objetos[6], "Los ataques básicos tienen la habilidad de desarmar al rival,"
                                                                     " prohibiendo el que ataquen durante 3 segundos")
Guantelete_Armadura = Combinacion("Guantelete Armadura", Objetos[5], Objetos[7], "Después de castear un spell, los siguientes "
                                                                                 "ataques basicos congelan durante 1.5 segundos")

#Todas las combinaciones de Fajin de Mercurio
Dragon_claw = Combinacion("Dragon Claw", Objetos[6], Objetos [6], "50% de resistencia a daño mágico")
Quicksilver = Combinacion("Quicksilver", Objetos[6], Objetos[7], "Inmune al CC")

#Todas las combinaciones de Guante critico
Guantelete_Critico = Combinacion("Guantelete Critico", Objetos[7], Objetos[7], "Da dos objetos al azar al usuario que son mejores"
                                                                               "segun subes TU de nivel. No se puedene equipar otros"
                                                                               "objetos")

#Todas las combinaciones de espatula
Yuumus = Combinacion("Yuumus", Objetos[8], Objetos[0], "Usuario es Asesino")
Llama = Combinacion ("Llama", Objetos[8], Objetos[1], "El usuario es Inferno")
Blade_Ruined = Combinacion("Blade Ruined King", Objetos[8], Objetos[2], "El usuario es Blademaster")
Gorro = Combinacion ("Gorro de Mago", Objetos[8], Objetos[3], "El usuario es mage")
Frozen_Mallet = Combinacion("Frozen Mallet", Objetos[8], Objetos[4], "El usuario es glacial")
Warden_Mail = Combinacion("Warden Mail", Objetos[8], Objetos[5], "El usuario es Warden")
Talisman = Combinacion("Talisman de Luz", Objetos[8], Objetos[6], "El usuario es de luz")
B_Cleaver = Combinacion("Black Cleaver", Objetos[8], Objetos[7], "El usuario es Berseker")
F_Nature = Combinacion("Force of Nature", Objetos[8], Objetos[8], "Se puede añadir una unidad más al tablero")

#Creamos lista que contiene todos los objetos de combinacion.
listaObjetosCombinacion = [Espada_de_la_Muerte, Sable_Pistola, Asesino_de_Gigantes, Shojin, Heraldo_Zeke, Angel_Guardian,
                           Sanguinaria, Filo_Infinito, Gorro_Rabadon, Guinsoo, Luden_Echo, Morello, Solaris, Ionic_Spark,
                           Guantelete_AP, Rapid_FireCannon, Statikk_Shiv, Hydra, Titans_Resolve, Runaan_Hurricane,
                           Ultimas_Palabras, Baston_Arcangel, Redencion, Corazon_hielo, Hush, Guantelete_Mana,
                           Warmog, Bufo_Rojo, Zephyr, Guantelete_Vida, Malla_Espinas, Sword_Breaker, Guantelete_Armadura,
                           Dragon_claw, Quicksilver, Guantelete_Critico, Yuumus, Llama, Blade_Ruined, Gorro, Frozen_Mallet,
                           Warden_Mail, Talisman, B_Cleaver, F_Nature]


##                                   !!!FUNCIONES!!!!

#Funcion para averiguar objetos de combinación a raíz de sus objetos
def averiguarObjetosComb(n, li):
    #Recorremos la lista y verificamos si la respuesta que damos es igual a la que esta guardada en el objeto
    #Convertimos todo en upper case para que no haya disparidad
    contador = 0
    random.shuffle(li)
    for obj in li:
        print ("¿Qué objeto esta compuesto de los siguientes objetos: ")
        print (Combinacion.getObjetosComp(obj))
        respuesta = str(input())
        if (respuesta.upper() == Combinacion.getNombreObjeto(obj).upper()):
            print ("\n\tTu respuesta es correcta :)!!! Aquí tienes la descripción del objeto: ")
        else:
            print ("\n\tHas fallado :(!!! Aquí tienes la descripción del objeto: \n")
        print (Combinacion.printObj(obj))
        print("****************************\n")
        contador = contador + 1
        if (contador >= n):
            break

#Función inversa a la anterior. Dar los objetos a partir
def averiguarObjetosPeques(n, li):
    contador = 0
    random.shuffle(li)
    for obj in li:
        print ("¿De qué objetos está formado: " + Combinacion.getNombreObjeto(obj))
        print ("\nPosibilidades: " + Objetos[0] + ", " + Objetos[1] + ", " + Objetos[2]+ ", " + Objetos[3]+ ", " +Objetos[4]+ ", " + Objetos[5]+ ", " +
               Objetos[6]+ ", " + Objetos[7]+ ", " + Objetos [8])
        print ("\nSELECCIONA EL OBJETO NÚMERO 1: ")
        elemento1 = str(input())
        print("SELECCIONA EL OBJETO NÚMERO 2: ")
        elemento2 = str(input())
        listaElementos = [elemento1.lower(), elemento2.lower()]
        listaElementos.sort()
        listaO = Combinacion.getObjetosComp(obj).copy()
        listaO.sort()
        primeraCon = listaElementos[0] == listaO[0]
        segundaCon = listaElementos[1] == listaO[1]
        if (primeraCon and segundaCon):
            print("\n\tTu respuesta es correcta :)!!! Aquí tienes la descripción del objeto: \n")
        else:
            print("\n\tHas fallado :(!!! Aquí tienes la descripción del objeto: ")
        print(Combinacion.printObj(obj))
        print("****************************\n")
        contador = contador + 1
        if (contador >= n):
            break
#Funcion para crear archivos de texto con el nombre de los objetos y los objetos que lo forman

def imprimir (li, objsimples):
    f = open("Nombre_Objetos_por_Yoti.txt", "w+")
    f.write("NOMBRE DE OBJETOS SIMPLES: \n\n")
    for objsim in objsimples:
        f.write(objsim + "\n")
    f.write ("*********************\n\n")
    f.write ("NOMBRE DE OBJETOS COMPUESTOS:\n\n")
    for obj in li:
        f.write (Combinacion.getNombreObjeto(obj) +"\n")
    f.write ("\n\n ªª**************** \n  YOTIVISIONNNNNNNNNNNNNNNNNNNNNNNNNNN")
    f.close()




#BANNER
print(" _____  _   _  _____  _____  _____ ")
print("/  ___|| | | ||  _  ||_   _||_   _|")
print("\ `--. | |_| || | | |  | |    | |  ")
print(" `--. \|  _  || | | |  | |    | |  ")
print("/\__/ /| | | |\ \_/ /  | |   _| |_ ")
print("\____/ \_| |_/ \___/   \_/   \___/ ")
print("        _____ ______  _____              ")
print("       |_   _||  ___||_   _|             ")
print("         | |  | |_     | |               ")
print("         | |  |  _|    | |               ")
print("         | |  | |      | |               ")
print("         \_/  \_|      \_/               ")
print (" ")
print ("**** BIENVENIDO AL SHOTIPROGRAMA para aprenderse los objetos y las combinaciones en TFT ****")
print ("La función de este programita es practicar los objetos y campeones del TFT\n"
       "con el objetivo de tenerlo todo más interiorizado y ser más rapido in game.\n\n")

seleccion = 0
while (seleccion != 4):
    print ("Para hacer el test de Objetos a Objetos Combinados escribe 1.\n"
           "Para el test de Objetos Combinados a Objetos escribe 2.\n"
           "Para cerrar el programa escribe 4 o presiona varias veces Enter.\n"
           "Si escribes cualquier cosa diferente a un número el programa se cerrará.\n\n"
           "Futuras funcionalidades:\n" 
           "A)adivina la clase del campeón B)adivina que campeón falta en esta clase\n"
           "C)La posibilidad de cambiar el nombre a los objetos al gusto\n")

    seleccion = input()
    if (int(seleccion) == 1):
        print ("\n**********************\nHas seleccionado de objetos a objetos combinacionales, elige el numero de preguntas que quieres en el"
               " test: (Max 45)")
        numeroPreg = input()
        print ("\n**********************\nHas seleccionado: " + numeroPreg + " preguntas. Comienza el test: \n")
        averiguarObjetosComb(int(numeroPreg), listaObjetosCombinacion)
    elif (int(seleccion) ==2):
        print ("\n**********************\nHas seleccionado de objetos combinacionales a objetos, elige el numero de preguntas que quieres en el"
               " test: (Max 45)")
        numeroPreg = input()
        print ("\n**********************\nHas seleccionado: " + numeroPreg + " preguntas. Comienza el test: \n")
        averiguarObjetosPeques(int(numeroPreg), listaObjetosCombinacion)
        print ("")
    elif (int(seleccion) == 3):
        print ("\n**********************\nImprimiendo nombre de objetos y objetos combinacionales")
        imprimir(listaObjetosCombinacion, Objetos)
    elif (int(seleccion) == 4):
        break
    else:
        print("No has seleccionado una opción correcta \n")

