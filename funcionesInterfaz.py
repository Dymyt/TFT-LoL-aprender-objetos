from tkinter import *
from tkinter.ttk import *
from combinaciones import *
import random

#ESTA FUNCION CREA LA BASE DE DATOS DE LOS OBJETOS DEL JUEGO. AL FINAL DEVOLVEREMOS UN ARRAY CON TODOS LOS OBJETOS
#TODO SE HACE A TRAVÉS DE UNA CLASE
def basedeDatos ():
    #Cada objeto del juego en una lista para no equivocarnos al escribir una y otra vez
    Objetos = ["espadon", "vara", "arco", "lagrima", "cinturon", "armadura", "capa",
               "guante", "espatula"]

    #CREAMOS LOS OBJETOS DE COMBINACION

    #Todas las combinaciones de Espadón
    Espada_de_la_Muerte = Combinacion("Deathblade", Objetos[0], Objetos[0], "+15 de "
                                                                                     "AD por cada unidad que mate o asista en matar ")
    Sable_Pistola = Combinacion("Hextech Gunblade", Objetos[0], Objetos[1], "Curación del 25% del daño realizado, sin contar objetos")
    Asesino_de_Gigantes = Combinacion("Giant Slayer", Objetos [0], Objetos [2], "Autoataques hacen un daño adicional del 9%"
                                                                                       " de la vida actual del objetivo")
    Shojin = Combinacion("Spear of Shojin", Objetos[0], Objetos [3], "Ganas un 18% de tu maná máximo con cada autoataque después de haber realizado"
                                                            " tu ultimate")
    Heraldo_Zeke = Combinacion("Zeke's Herald", Objetos[0], Objetos[4], "Tu y tús aliados en 2 casillas a izq y der ganáis "
                                                                       "20% de velocidad de ataque")
    Angel_Guardian = Combinacion("Guardian Angel", Objetos[0], Objetos[5], "Al morir el usuario revive a los dos segundos con "
                                                                           "400 de vida")
    Sanguinaria = Combinacion("Bloodthirster", Objetos[0], Objetos[6], "Curación del 40% del daño de tus autoataques")
    Filo_Infinito = Combinacion("Infinity Edge", Objetos[0], Objetos[7], "Los ataques críticos pegan un 125% más")

    #Todas las combinaciones de Vara grande
    Gorro_Rabadon = Combinacion("Rabadon's Deathcap", Objetos [1], Objetos[1], "Incrementa el poder de habiliad un 75%")
    Guinsoo = Combinacion("Guinsoo's Blade", Objetos[1], Objetos[2], "4% de aumento de velocidad de ataque por Autoataque, stackea infinito")
    Luden_Echo = Combinacion("Luden's Echo", Objetos[1], Objetos[3], "Al usar el ultimate, el objetivo y hasta tres campeones más"
                                                                   " situados a max. 2 celdas reciben 120/160/220 de daño mágico"
                                                                    " dependiendo del nivel")
    Morello = Combinacion("Morellonomicon", Objetos[1], Objetos[4], "Los hechizos queman un 18% del hp máximo durante 10 segundos"
                                                             " y aplican heridas graves")
    Solaris = Combinacion("Solari's Locket", Objetos[1], Objetos[5], "Tú y tus aliados en 2 casillas a izq y der ganáis un escudo de"
                                                              " 250/275/300 dependiendo del nivel del campeon que lo tenga equipado")
    Ionic_Spark = Combinacion("Ionic Spark", Objetos[1], Objetos [6], "Los enemigos a 3 celdas que casteen su ultimate reciben "
                                                                        "200% de daño mágico de su mana máximo")
    Guantelete_AP = Combinacion("Jeweled Gauntlet", Objetos[1], Objetos[7], "Las habilidades de ap pueden hacer impactos críticos")

    #Todas las combinaciones de Arco de Velocidad
    Rapid_FireCannon = Combinacion("Rapid Firecannon", Objetos[2], Objetos[2], "Dobla el rango de los ataques")
    Statikk_Shiv = Combinacion ("Stattik Shiv", Objetos [2], Objetos [3], "Cada tercer ataque básico hace"
                                                                                            " 80 de daño mágico y a 2/3/4 enemigos"
                                                                                            " dependiendo del nivel del campeon")
    Hydra = Combinacion("Titanic Hydra", Objetos[2], Objetos [4], "Ataques Básicos hacen un 3% de daño adicional como daño mágico, e impacta"
                                                          " en los enemigos detras del objetivo adyacentes")
    Titans_Resolve = Combinacion("Titan's Resolve", Objetos[2], Objetos[5], "Cuando recibes daño o inglinges un impacto crítico consigues"
                                                                            " 2% de daño adicional para el resto del combate hasta 100%. A"
                                                                           " Stacks máximos se gana 25 de armadura y resistencia mágica")
    Runaan_Hurricane = Combinacion("Runaan's Hurricane", Objetos[2], Objetos[6], "Los ataques básicos impactan a un enemigo adicional con"
                                                                               " una potencia del 60%. Aplica efectos de impacto")
    Ultimas_Palabras = Combinacion("Last Whisper", Objetos[2], Objetos[7], "Los ataques básicos reducen la armadura del enemigo un"
                                                                               " 90% por 3 segundos")

    #Todas las combinaciones de Lágrima
    Baston_Arcangel = Combinacion("Seraph's Embrace", Objetos[3], Objetos[3], "Después de usar tu ultimate recuperas 20 de mana")
    Redencion = Combinacion("Redemption", Objetos[3], Objetos [4], "Cuando bajas del 30% de la vida castea un circulo que cura 1200 "
                                                                  "de vida despues de 2.5 sec de delay")
    Corazon_hielo = Combinacion("Frozen Heart", Objetos[3], Objetos[5], "Reduce la velocidad de ataque de los enemigos adyacentes"
                                                                            " un 40% por 0,5 segundos")
    Hush = Combinacion("Hush", Objetos[3], Objetos[6], "Los ataques básicos tienen un 20% de probabilidad de silenciar a los enemigos"
                                                       " durante 4 segundos")
    Guantelete_Mana = Combinacion("Hand of Justice", Objetos[3], Objetos[7], "Al inicio del turno puedes ganar realizar 50% más de daño"
                                                                             " con habilidades y ataques, o curarte 50 de vida por ataque")

    #Todas las combinaciones de Cinturon de Vida
    Warmog =  Combinacion("Warmog's Armor", Objetos[4], Objetos[4], "Ganar 6% de HP faltante cada segundo, máximo 400hp/s")
    Bufo_Rojo = Combinacion("Red Buff", Objetos[4], Objetos[5], "Cada AA aplica una quemadura que durante 10s infligirá el 18% de la"
                                                                 " vida máxima y reduciendo la curación, no se pueden aplicar 2 cargas")
    Zephyr = Combinacion("Zephyr", Objetos[4], Objetos[6], "Anula durante 6 segundos al campeon más cercano al lado opuesto del campeón"
                                                           " que lleve equipado este objeto")
    Guantelete_Vida = Combinacion("Trap Claw", Objetos[4], Objetos[7], "Al inicio de cada ronda ganas un escudo que bloquea el primer"
                                                                             " enemy spell recibido y stunea al enemigo por 4 segundos")

    #Todas las combinaciones con Armadura
    Malla_Espinas = Combinacion("Bramble Vest", Objetos[5], Objetos[5], "Niega el daño adicional de impactos criticos, Cuando recibe"
                                                                            " un autoataque hace 80/120/160 de daño magico a los enemigos"
                                                                            " cercanos")
    Sword_Breaker = Combinacion("Sword Breaker", Objetos[5], Objetos[6], "Los ataques básicos tienen la habilidad de desarmar al rival,"
                                                                         " prohibiendo el que ataquen durante 3 segundos")
    Guantelete_Armadura = Combinacion("Iceborn Gauntlet", Objetos[5], Objetos[7], "Después de castear un spell, los siguientes "
                                                                                     "ataques basicos congelan durante 1.5 segundos")

    #Todas las combinaciones de Fajin de Mercurio
    Dragon_claw = Combinacion("Dragon's Claw", Objetos[6], Objetos [6], "50% de resistencia a daño mágico")
    Quicksilver = Combinacion("Quicksilver", Objetos[6], Objetos[7], "Inmune al CC")

    #Todas las combinaciones de Guante critico
    Guantelete_Critico = Combinacion("Thief's Gloves", Objetos[7], Objetos[7], "Da dos objetos al azar al usuario que son mejores"
                                                                                   "segun subes TU de nivel. No se puedene equipar otros"
                                                                                   "objetos")

    #Todas las combinaciones de espatula
    Yuumus = Combinacion("Youmuu's Ghostblade", Objetos[8], Objetos[0], "Usuario es Asesino")
    Llama = Combinacion ("Inferno Cinder", Objetos[8], Objetos[1], "El usuario es Inferno")
    Blade_Ruined = Combinacion("Blade of the Ruined King", Objetos[8], Objetos[2], "El usuario es Blademaster")
    Gorro = Combinacion ("Mage's Cap", Objetos[8], Objetos[3], "El usuario es mage")
    Frozen_Mallet = Combinacion("Frozen Mallet", Objetos[8], Objetos[4], "El usuario es glacial")
    Warden_Mail = Combinacion("Warden's Mail", Objetos[8], Objetos[5], "El usuario es Warden")
    Talisman = Combinacion("Talisman of Light", Objetos[8], Objetos[6], "El usuario es de luz")
    B_Cleaver = Combinacion("Berseker Axe", Objetos[8], Objetos[7], "El usuario es Berseker")
    F_Nature = Combinacion("Force of Nature", Objetos[8], Objetos[8], "Se puede añadir una unidad más al tablero")

    #Creamos lista que contiene todos los objetos de combinacion.
    listaObjetosCombinacion = [Espada_de_la_Muerte, Sable_Pistola, Asesino_de_Gigantes, Shojin, Heraldo_Zeke, Angel_Guardian,
                               Sanguinaria, Filo_Infinito, Gorro_Rabadon, Guinsoo, Luden_Echo, Morello, Solaris, Ionic_Spark,
                               Guantelete_AP, Rapid_FireCannon, Statikk_Shiv, Hydra, Titans_Resolve, Runaan_Hurricane,
                               Ultimas_Palabras, Baston_Arcangel, Redencion, Corazon_hielo, Hush, Guantelete_Mana,
                               Warmog, Bufo_Rojo, Zephyr, Guantelete_Vida, Malla_Espinas, Sword_Breaker, Guantelete_Armadura,
                               Dragon_claw, Quicksilver, Guantelete_Critico, Yuumus, Llama, Blade_Ruined, Gorro, Frozen_Mallet,
                               Warden_Mail, Talisman, B_Cleaver, F_Nature]
    return listaObjetosCombinacion

##                                   !!!FUNCIONES!!!!

#Función adivinar objetos
def ObjetoRandom():
    listaRandom = basedeDatos()
    random.shuffle(listaRandom)
    return (Combinacion.getNombreObjeto(listaRandom[0]))

#Funcion que comprueba si hemos acertado o no
def comprobandoAcierto(objeto1, objeto2, objetoComp):
    print (objeto1, objeto2, objetoComp)
    listaElementosPropuesta = [str(objeto1), str(objeto2)]
    listaElementosPropuesta.sort()
    listaElementos = objetosSimples(objetoComp).copy()
    listaElementos.sort()
    primeraCon = str(listaElementos[0]) == str(listaElementosPropuesta[0])
    segundaCon = str(listaElementos[1]) == str(listaElementosPropuesta[1])
    if primeraCon and segundaCon:
        return "!!HAS ACERTADO!!"
    else:
        return "!!HAS FALLADO!!"


#Devuelve una lista de los objetos de los que está compuesto un objeto evolucionado
def objetosSimples(objetoComp):
    listaObjetos = basedeDatos()
    for obj in listaObjetos:
        if Combinacion.getNombreObjeto(obj) == str(objetoComp):
            return Combinacion.getObjetosComp(obj)
            break

#ImprimirDescripcion
def objetoDescripcion(objetoComp):
    listaObjetos = basedeDatos()
    for obj in listaObjetos:
        if Combinacion.getNombreObjeto(obj) == str(objetoComp):
            return Combinacion.printObj(obj)
            break