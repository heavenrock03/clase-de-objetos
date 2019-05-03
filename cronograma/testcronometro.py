from cronometro import *

c = cronometro()
c.settiempo("01:10:01:05")
for i in range (5000):
    c.retroceder()
    print c.gettiempo() 

