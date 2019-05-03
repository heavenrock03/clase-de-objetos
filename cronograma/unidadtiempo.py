class unidadtiempo():
    def __init__(self):
        self.valor=0
        self.tope=0
    def avanzar(self):
        if self.valor < self.tope:
            self.valor += 1
        else:
            self.valor = 0
    def getvalor (self):
        return self.valor

    def gettope (self):
        return self.tope

    def retroceder(self):
        if self.valor == 0:
            self.valor = self.tope
        else:
            self.valor -=1
            
    def setvalor (self,v):
        self.valor = v 
