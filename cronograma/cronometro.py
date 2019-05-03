from hora import *
from minuto import *
from segundo import *
from decima import *

class cronometro():
    def __init__(self):
        self.h = hora()
        self.m = minuto()
        self.s = segundo()
        self.d = decima()

    def avanzar(self):
        self.d.avanzar()
        if self.d.getvalor()==0:
            self.s.avanzar()
            if self.s.getvalor()==0:
                self.m.avanzar()
                if self.m.getvalor()==0:
                    self.h.avanzar()

    def gettiempo(self):
        return "{:02d}".format(self.h.getvalor())+":"+"{:02d}".format(self.m.getvalor())+":"+"{:02d}".format(self.s.getvalor())+":"+"{:02d}".format(self.d.getvalor())

        
        
    def settiempo(self,x):
        v=x.split(":")
        self.h.setvalor(int(v[0]))
        self.m.setvalor(int(v[1]))
        self.s.setvalor(int(v[2]))
        self.d.setvalor(int(v[3]))

       
        
  
    def retroceder(self):
        self.d.retroceder()
        if self.d.getvalor()==self.d.gettope():
            self.s.retroceder()
            if self.s.getvalor()==self.s.gettope():
                self.m.retroceder()
                if self.m.getvalor()==self.m.gettope():
                    self.h.retroceder()

    
