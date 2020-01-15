from tkinter import *
from tkinter.ttk import *
from funcionesInterfaz import *


#Inicio, tamaño y nombre
root = Tk()
root.geometry("650x500")
root.title ("SHOTI TFT")


#################FUNCIONES y variables###############

variableCambio = IntVar()
variableCambio.set(1)
variableBoton = IntVar()
variablePrimerObjeto = StringVar()
variableSegundoObjeto = StringVar()
textoEnWidget = StringVar()
variableAdivinar= StringVar()
variableAcierto = StringVar()
variableDescripcion = StringVar()
#Las funciones de darle a un boton. Ademas guarda en una variable el nombre del objeto:
def cambioBotonSeleccion():

    if variableCambio.get() == 1:
        if variableBoton.get() == 0:
            botonSel1 = Button(frameSeleccion, image=espadonImagen).grid(row=0, column=1)
            variablePrimerObjeto.set("espadon")
        elif variableBoton.get() == 1:
            botonSel1 = Button(frameSeleccion, image=arcoImagen).grid(row=0, column=1)
            variablePrimerObjeto.set("arco")
        elif variableBoton.get() == 2:
            botonSel1 = Button(frameSeleccion, image=lagrimaImagen).grid(row=0, column=1)
            variablePrimerObjeto.set("lagrima")
        elif variableBoton.get() == 3:
            botonSel1 = Button(frameSeleccion, image=armaduraImagen).grid(row=0, column=1)
            variablePrimerObjeto.set("armadura")
        elif variableBoton.get() == 4:
            botonSel1 = Button(frameSeleccion, image=cinturonImagen).grid(row=0, column=1)
            variablePrimerObjeto.set("cinturon")
        elif variableBoton.get() == 5:
            botonSel1 = Button(frameSeleccion, image=espatulaImagen).grid(row=0, column=1)
            variablePrimerObjeto.set("espatula")
        elif variableBoton.get() == 6:
            botonSel1 = Button(frameSeleccion, image=fajinImagen).grid(row=0, column=1)
            variablePrimerObjeto.set("capa")
        elif variableBoton.get() == 7:
            botonSel1 = Button(frameSeleccion, image=guanteImagen).grid(row=0, column=1)
            variablePrimerObjeto.set("guante")
        elif variableBoton.get() == 8:
            botonSel1 = Button(frameSeleccion, image=varaImagen).grid(row=0, column=1)
            variablePrimerObjeto.set("vara")
        variableCambio.set(2)
    else:
        if variableBoton.get() == 0:
            botonSel2 = Button(frameSeleccion, image=espadonImagen).grid(row=0, column=2)
            variableSegundoObjeto.set("espadon")
        elif variableBoton.get() == 1:
            botonSel2 = Button(frameSeleccion, image=arcoImagen).grid(row=0, column=2)
            variableSegundoObjeto.set("arco")
        elif variableBoton.get() == 2:
            botonSel2 = Button(frameSeleccion, image=lagrimaImagen).grid(row=0, column=2)
            variableSegundoObjeto.set("lagrima")
        elif variableBoton.get() == 3:
            botonSel2 = Button(frameSeleccion, image=armaduraImagen).grid(row=0, column=2)
            variableSegundoObjeto.set("armadura")
        elif variableBoton.get() == 4:
            botonSel2 = Button(frameSeleccion, image=cinturonImagen).grid(row=0, column=2)
            variableSegundoObjeto.set("cinturon")
        elif variableBoton.get() == 5:
            botonSel2 = Button(frameSeleccion, image=espatulaImagen).grid(row=0, column=2)
            variableSegundoObjeto.set("espatula")
        elif variableBoton.get() == 6:
            botonSel2 = Button(frameSeleccion, image=fajinImagen).grid(row=0, column=2)
            variableSegundoObjeto.set("capa")
        elif variableBoton.get() == 7:
            botonSel2 = Button(frameSeleccion, image=guanteImagen).grid(row=0, column=2)
            variableSegundoObjeto.set("guante")
        elif variableBoton.get() == 8:
            botonSel2 = Button(frameSeleccion, image=varaImagen).grid(row=0, column=2)
            variableSegundoObjeto.set("vara")
        variableCambio.set(1)

def botonEspadon():
    variableBoton.set(0)
    cambioBotonSeleccion()
def botonArco():
    variableBoton.set(1)
    cambioBotonSeleccion()
def botonLagrima():
    variableBoton.set(2)
    cambioBotonSeleccion()
def botonArmadura():
    variableBoton.set(3)
    cambioBotonSeleccion()
def botonCinturon():
    variableBoton.set(4)
    cambioBotonSeleccion()
def botonEspatula():
    variableBoton.set(5)
    cambioBotonSeleccion()
def botonFajin():
    variableBoton.set(6)
    cambioBotonSeleccion()
def botonGuante():
    variableBoton.set(7)
    cambioBotonSeleccion()
def botonVara():
    variableBoton.set(8)
    cambioBotonSeleccion()

def siguienteObjeto():
    variableAdivinar.set(ObjetoRandom())
    textoPantalla.delete('1.0', END)
    textoPantalla.insert(INSERT, "Selecciona los objetos simples que componen el objeto:\n")
    textoPantalla.insert(INSERT, variableAdivinar.get())
    if (variableAdivinar.get() == "Deathblade"):
        imagenObjetosCombBoton = Button(frameIntermedio, image=imagen01).grid(row=0, column=1)
    elif (variableAdivinar.get() == "Hextech Gunblade"):
        imagenObjetosCombBoton = Button(frameIntermedio, image=imagen02).grid(row=0, column=1)
    elif (variableAdivinar.get() == "Giant Slayer"):
        imagenObjetosCombBoton = Button(frameIntermedio, image=imagen03).grid(row=0, column=1)
    elif (variableAdivinar.get() == "Spear of Shojin"):
        imagenObjetosCombBoton = Button(frameIntermedio, image=imagen04).grid(row=0, column=1)
    elif (variableAdivinar.get() == "Zeke's Herald"):
        imagenObjetosCombBoton = Button(frameIntermedio, image=imagen05).grid(row=0, column=1)
    elif (variableAdivinar.get() == "Guardian Angel"):
        imagenObjetosCombBoton = Button(frameIntermedio, image=imagen06).grid(row=0, column=1)
    elif (variableAdivinar.get() == "Bloodthirster"):
        imagenObjetosCombBoton = Button(frameIntermedio, image=imagen07).grid(row=0, column=1)
    elif (variableAdivinar.get() == "Infinity Edge"):
        imagenObjetosCombBoton = Button(frameIntermedio, image=imagen08).grid(row=0, column=1)
    elif (variableAdivinar.get() == "Rabadon's Deathcap"):
        imagenObjetosCombBoton = Button(frameIntermedio, image=imagen09).grid(row=0, column=1)
    elif (variableAdivinar.get() == "Guinsoo's Blade"):
        imagenObjetosCombBoton = Button(frameIntermedio, image=imagen10).grid(row=0, column=1)
    elif (variableAdivinar.get() == "Luden's Echo"):
        imagenObjetosCombBoton = Button(frameIntermedio, image=imagen11).grid(row=0, column=1)
    elif (variableAdivinar.get() == "Morellonomicon"):
        imagenObjetosCombBoton = Button(frameIntermedio, image=imagen12).grid(row=0, column=1)
    elif (variableAdivinar.get() == "Solari's Locket"):
        imagenObjetosCombBoton = Button(frameIntermedio, image=imagen13).grid(row=0, column=1)
    elif (variableAdivinar.get() == "Ionic Spark"):
        imagenObjetosCombBoton = Button(frameIntermedio, image=imagen14).grid(row=0, column=1)
    elif (variableAdivinar.get() == "Jeweled Gauntlet"):
        imagenObjetosCombBoton = Button(frameIntermedio, image=imagen15).grid(row=0, column=1)
    elif (variableAdivinar.get() == "Rapid Firecannon"):
        imagenObjetosCombBoton = Button(frameIntermedio, image=imagen16).grid(row=0, column=1)
    elif (variableAdivinar.get() == "Stattik Shiv"):
        imagenObjetosCombBoton = Button(frameIntermedio, image=imagen17).grid(row=0, column=1)
    elif (variableAdivinar.get() == "Titanic Hydra"):
        imagenObjetosCombBoton = Button(frameIntermedio, image=imagen18).grid(row=0, column=1)
    elif (variableAdivinar.get() == "Titan's Resolve"):
        imagenObjetosCombBoton = Button(frameIntermedio, image=imagen19).grid(row=0, column=1)
    elif (variableAdivinar.get() == "Runaan's Hurricane"):
        imagenObjetosCombBoton = Button(frameIntermedio, image=imagen20).grid(row=0, column=1)
    elif (variableAdivinar.get() == "Last Whisper"):
        imagenObjetosCombBoton = Button(frameIntermedio, image=imagen21).grid(row=0, column=1)
    elif (variableAdivinar.get() == "Seraph's Embrace"):
        imagenObjetosCombBoton = Button(frameIntermedio, image=imagen22).grid(row=0, column=1)
    elif (variableAdivinar.get() == "Redemption"):
        imagenObjetosCombBoton = Button(frameIntermedio, image=imagen23).grid(row=0, column=1)
    elif (variableAdivinar.get() == "Frozen Heart"):
        imagenObjetosCombBoton = Button(frameIntermedio, image=imagen24).grid(row=0, column=1)
    elif (variableAdivinar.get() == "Hush"):
        imagenObjetosCombBoton = Button(frameIntermedio, image=imagen25).grid(row=0, column=1)
    elif (variableAdivinar.get() == "Hand of Justice"):
        imagenObjetosCombBoton = Button(frameIntermedio, image=imagen26).grid(row=0, column=1)
    elif (variableAdivinar.get() == "Warmog's Armor"):
        imagenObjetosCombBoton = Button(frameIntermedio, image=imagen27).grid(row=0, column=1)
    elif (variableAdivinar.get() == "Red Buff"):
        imagenObjetosCombBoton = Button(frameIntermedio, image=imagen28).grid(row=0, column=1)
    elif (variableAdivinar.get() == "Zephyr"):
        imagenObjetosCombBoton = Button(frameIntermedio, image=imagen29).grid(row=0, column=1)
    elif (variableAdivinar.get() == "Trap Claw"):
        imagenObjetosCombBoton = Button(frameIntermedio, image=imagen30).grid(row=0, column=1)
    elif (variableAdivinar.get() == "Bramble Vest"):
        imagenObjetosCombBoton = Button(frameIntermedio, image=imagen31).grid(row=0, column=1)
    elif (variableAdivinar.get() == "Sword Breaker"):
        imagenObjetosCombBoton = Button(frameIntermedio, image=imagen32).grid(row=0, column=1)
    elif (variableAdivinar.get() == "Iceborn Gauntlet"):
        imagenObjetosCombBoton = Button(frameIntermedio, image=imagen33).grid(row=0, column=1)
    elif (variableAdivinar.get() == "Dragon's Claw"):
        imagenObjetosCombBoton = Button(frameIntermedio, image=imagen34).grid(row=0, column=1)
    elif (variableAdivinar.get() == "Quicksilver"):
        imagenObjetosCombBoton = Button(frameIntermedio, image=imagen35).grid(row=0, column=1)
    elif (variableAdivinar.get() == "Thief's Gloves"):
        imagenObjetosCombBoton = Button(frameIntermedio, image=imagen36).grid(row=0, column=1)
    elif (variableAdivinar.get() == "Youmuu's Ghostblade"):
        imagenObjetosCombBoton = Button(frameIntermedio, image=imagen37).grid(row=0, column=1)
    elif (variableAdivinar.get() == "Inferno Cinder"):
        imagenObjetosCombBoton = Button(frameIntermedio, image=imagen38).grid(row=0, column=1)
    elif (variableAdivinar.get() == "Blade of the Ruined King"):
        imagenObjetosCombBoton = Button(frameIntermedio, image=imagen39).grid(row=0, column=1)
    elif (variableAdivinar.get() == "Mage's Cap"):
        imagenObjetosCombBoton = Button(frameIntermedio, image=imagen40).grid(row=0, column=1)
    elif (variableAdivinar.get() == "Frozen Mallet"):
        imagenObjetosCombBoton = Button(frameIntermedio, image=imagen41).grid(row=0, column=1)
    elif (variableAdivinar.get() == "Warden's Mail"):
        imagenObjetosCombBoton = Button(frameIntermedio, image=imagen42).grid(row=0, column=1)
    elif (variableAdivinar.get() == "Talisman of Light"):
        imagenObjetosCombBoton = Button(frameIntermedio, image=imagen43).grid(row=0, column=1)
    elif (variableAdivinar.get() == "Berseker Axe"):
        imagenObjetosCombBoton = Button(frameIntermedio, image=imagen44).grid(row=0, column=1)
    elif (variableAdivinar.get() == "Force of Nature"):
        imagenObjetosCombBoton = Button(frameIntermedio, image=imagen45).grid(row=0, column=1)
    else:
        imagenObjetosCombBoton = Button(frameIntermedio, image=imagenObjetosComb).grid(row=0, column=1)


#Boton Siguiente

def presionarSiguiente():
    textoPantalla.delete('1.0', END)
    variableAcierto.set (comprobandoAcierto(variablePrimerObjeto.get(), variableSegundoObjeto.get(), variableAdivinar.get()))
    textoPantalla.insert(INSERT,  variableAcierto.get())
    variableDescripcion.set(objetoDescripcion(variableAdivinar.get()))
    textoPantalla.insert(INSERT, "\n")
    textoPantalla.insert(INSERT, variableDescripcion.get())
#//////////////FUNCIONES y variables///////////////////

#Creacion de frames para separar las cosas
frameArriba = Frame(root)
frameArriba.pack()
frameIntermedio = Frame(root)
frameIntermedio.pack()
frameObjetos = Frame(root)
frameObjetos.pack()
frameSeparacion = Frame(root)
frameSeparacion.pack()
frameSeleccion = Frame(root)
frameSeleccion.pack()


textoACambiar= StringVar()
textoACambiar.set("Esto es el texto a cambiar")

#Creamos parte de arriba e intermedia
imagenTitulo = PhotoImage(file =r"G:\untitled\imagenes\titulo.png")
titulo1 = Label(frameArriba, image = imagenTitulo).pack()

imagenObjetosComb = PhotoImage(file=r"G:\untitled\imagenes\objetoprincipio.png")
imagenObjetosCombBoton = Button(frameIntermedio, image=imagenObjetosComb).grid(row=0, column=1)

textoPantalla = Text(frameIntermedio, bg = "white", bd = 3, height = 5, width = 60)
textoPantalla.grid(row=0, column=0, padx = 10, pady = 20)
#Hay que separar el .grid de la creacion para poder hacer funciones sobre el


#Creamos los botenes con sus imágenes*********************************************
espadonImagen = PhotoImage(file = r"G:\untitled\imagenes\espadon.png")
espadonBoton = Button(frameObjetos, image = espadonImagen, cursor = "cross", command= botonEspadon).grid(row=0, column =0)

arcoImagen = PhotoImage(file = r"G:\untitled\imagenes\arco.png")
arcoBoton = Button(frameObjetos, image = arcoImagen, cursor = "cross", command= botonArco).grid(row=0, column = 1)

lagrimaImagen = PhotoImage(file = r"G:\untitled\imagenes\lagrima.png")
lagrimaBoton = Button(frameObjetos, image = lagrimaImagen, cursor = "cross", command = botonLagrima).grid(row=0, column = 2)

armaduraImagen = PhotoImage(file = r"G:\untitled\imagenes\armadura.png")
armaduraBoton = Button(frameObjetos, image = armaduraImagen, cursor = "cross", command = botonArmadura).grid(row=0, column = 3)

cinturonImagen = PhotoImage(file = r"G:\untitled\imagenes\cinturon.png")
cinturonBoton = Button(frameObjetos, image = cinturonImagen, cursor = "cross", command= botonCinturon).grid(row=0, column = 4)

espatulaImagen = PhotoImage(file = r"G:\untitled\imagenes\espatula.png")
espatulaBoton = Button(frameObjetos, image = espatulaImagen, cursor = "cross", command= botonEspatula).grid(row=1, column = 0)

fajinImagen = PhotoImage(file = r"G:\untitled\imagenes\fajin.png")
fajinBoton = Button(frameObjetos, image = fajinImagen, cursor = "cross", command= botonFajin).grid(row=1, column = 1)

guanteImagen = PhotoImage(file = r"G:\untitled\imagenes\guante.png")
guanteBoton = Button(frameObjetos, image = guanteImagen, cursor = "cross", command= botonGuante).grid(row=1, column = 2)

varaImagen = PhotoImage(file = r"G:\untitled\imagenes\vara.png")
varaBoton = Button(frameObjetos, image = varaImagen, cursor = "cross", command= botonVara).grid(row=1, column = 3)
#Creamos los botenes con sus imágenes*********************************************

#Creamos la parte inferior

imagenSeparacion = PhotoImage(file = r"G:\untitled\imagenes\separacion.png")
botonSeparacion = Label(frameSeparacion, image = imagenSeparacion).grid(row=0, column=0, pady = 15)

textoSeleccion = Label(frameSeleccion, text = "TU SELECCIÓN:  ").grid(row=0, column =0, pady = 10)

botonSel1 = Button(frameSeleccion,image=imagenObjetosComb).grid(row=0, column = 1)
botonSel2 = Button(frameSeleccion,image=imagenObjetosComb).grid(row=0, column = 2, padx= 5)

botonSiguiente = Button(frameSeleccion, text="Siguiente", command = presionarSiguiente).grid(row =0, column = 3, padx =10)
botonSiguienteObjeto = Button(frameIntermedio, text="Siguiente Objeto", command = siguienteObjeto).grid(row =1, column = 1, pady= 5)


































#Imagenes de objetos Combinacionales
imagen01 = PhotoImage(file = r"G:\untitled\imagenes\comb\01.png")
imagen02 = PhotoImage(file = r"G:\untitled\imagenes\comb\02.png")
imagen03 = PhotoImage(file = r"G:\untitled\imagenes\comb\03.png")
imagen04 = PhotoImage(file = r"G:\untitled\imagenes\comb\04.png")
imagen05 = PhotoImage(file = r"G:\untitled\imagenes\comb\05.png")
imagen06 = PhotoImage(file = r"G:\untitled\imagenes\comb\06.png")
imagen07 = PhotoImage(file = r"G:\untitled\imagenes\comb\07.png")
imagen08 = PhotoImage(file = r"G:\untitled\imagenes\comb\08.png")
imagen09 = PhotoImage(file = r"G:\untitled\imagenes\comb\09.png")
imagen10 = PhotoImage(file = r"G:\untitled\imagenes\comb\10.png")
imagen11 = PhotoImage(file = r"G:\untitled\imagenes\comb\11.png")
imagen12 = PhotoImage(file = r"G:\untitled\imagenes\comb\12.png")
imagen13 = PhotoImage(file = r"G:\untitled\imagenes\comb\13.png")
imagen14 = PhotoImage(file = r"G:\untitled\imagenes\comb\14.png")
imagen15 = PhotoImage(file = r"G:\untitled\imagenes\comb\15.png")
imagen16 = PhotoImage(file = r"G:\untitled\imagenes\comb\16.png")
imagen17 = PhotoImage(file = r"G:\untitled\imagenes\comb\17.png")
imagen18 = PhotoImage(file = r"G:\untitled\imagenes\comb\18.png")
imagen19 = PhotoImage(file = r"G:\untitled\imagenes\comb\19.png")
imagen20 = PhotoImage(file = r"G:\untitled\imagenes\comb\20.png")
imagen21 = PhotoImage(file = r"G:\untitled\imagenes\comb\21.png")
imagen22 = PhotoImage(file = r"G:\untitled\imagenes\comb\22.png")
imagen23 = PhotoImage(file = r"G:\untitled\imagenes\comb\23.png")
imagen24 = PhotoImage(file = r"G:\untitled\imagenes\comb\24.png")
imagen25 = PhotoImage(file = r"G:\untitled\imagenes\comb\25.png")
imagen26 = PhotoImage(file = r"G:\untitled\imagenes\comb\26.png")
imagen27 = PhotoImage(file = r"G:\untitled\imagenes\comb\27.png")
imagen28 = PhotoImage(file = r"G:\untitled\imagenes\comb\28.png")
imagen29 = PhotoImage(file = r"G:\untitled\imagenes\comb\29.png")
imagen30 = PhotoImage(file = r"G:\untitled\imagenes\comb\30.png")
imagen31 = PhotoImage(file = r"G:\untitled\imagenes\comb\31.png")
imagen32 = PhotoImage(file = r"G:\untitled\imagenes\comb\32.png")
imagen33 = PhotoImage(file = r"G:\untitled\imagenes\comb\33.png")
imagen34 = PhotoImage(file = r"G:\untitled\imagenes\comb\34.png")
imagen35 = PhotoImage(file = r"G:\untitled\imagenes\comb\35.png")
imagen36 = PhotoImage(file = r"G:\untitled\imagenes\comb\36.png")
imagen37 = PhotoImage(file = r"G:\untitled\imagenes\comb\37.png")
imagen38 = PhotoImage(file = r"G:\untitled\imagenes\comb\38.png")
imagen39 = PhotoImage(file = r"G:\untitled\imagenes\comb\39.png")
imagen40 = PhotoImage(file = r"G:\untitled\imagenes\comb\40.png")
imagen41 = PhotoImage(file = r"G:\untitled\imagenes\comb\41.png")
imagen42 = PhotoImage(file = r"G:\untitled\imagenes\comb\42.png")
imagen43 = PhotoImage(file = r"G:\untitled\imagenes\comb\43.png")
imagen44 = PhotoImage(file = r"G:\untitled\imagenes\comb\44.png")
imagen45 = PhotoImage(file = r"G:\untitled\imagenes\comb\45.png")

#Sirve para recorrer constantemente este codigo y que no se cierre la ventana a menos que pinchemos en la x
root.mainloop()