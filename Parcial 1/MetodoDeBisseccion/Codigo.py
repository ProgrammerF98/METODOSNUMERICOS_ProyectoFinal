#Ejemplo del paracaidas
import math
import numpy as np #es una librería para graficar.
import matplotlib.pyplot as plt #también para graficar.

def fun(c):
    return c**3 - 7*c**2 + 14*c - 6

arrayLen = 100
cIni = 0 #Primer intervalo
cEnd = 10 #Segundo intervalo
carray = np.linspace(cIni, cEnd, arrayLen)
fcarray = np.zeros(arrayLen)

for i in range(arrayLen):
    fcarray[i] = fun(carray[i])
    
plt.plot(carray, fcarray)
plt.grid()

c0 = 3.2
c1 = 4
maxIter = 100
itera = 0
for i in range(maxIter):
    itera += 1
    fc0 = fun(c0)
    fc1 = fun(c1)
    if fc0 * fc1 > 0:
        print("No hay raíz en este rango")
        break
    cr = (c0 + c1) /2 #Aquí es donde cambias lo de la regla falsa
    fcr = fun(cr)
    if fc0 * fcr < 0:
        c1 = cr
    else:
        c0 = cr
    if abs(fcr) < 0.0001:
        break
        
print("La raíz es %.5f"%c0)
print("Numero de Iteraciones %i"%itera)
