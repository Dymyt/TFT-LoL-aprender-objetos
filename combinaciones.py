class Combinacion:
    def __init__(self, nombreobjeto, objeto1, objeto2, descripcion):
        self.nombreobjeto = nombreobjeto
        self.objeto1 = objeto1
        self.objeto2 = objeto2
        self.descripcion = descripcion

    def getObjetosComp(self):
        return [self.objeto1, self.objeto2]

    def getNombreObjeto(self):
        return self.nombreobjeto

    def printObj(self):
        return self.nombreobjeto + "= " + "[" + self.objeto1 + ", " + self.objeto2 + "] Descripción: " + self.descripcion


