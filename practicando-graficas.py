# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 19:35:23 2019

@author: Luis
"""

#%%
#lista es con []
lista1 = [1,2,3,4,5]
# convertir tupla a listas
lista2= list((1,2,3,4,5))
#crear lista de un solo valor
lista3=[10]
# crear lista vacia
lista4= []

print(lista1)
print(lista2)
print(lista3)
print(lista4)

print(type(lista1))

#la lista a diferencia de una tupla, es un tipo de dato "mutable"
print(" ")
print(lista1)
lista1[0]=100
print(lista1)

print("primer valor de la lista: ", lista1[0])
print("ultimo valor de la lista: ", lista1[-1])

lista1= [10, 20,30 ,40 ,50]
for i in range(len(lista1)):
    print(lista1[i])
print()
for num in lista1:
    print(num)

for i, v in enumerate([10,20,30,40,50]):
    print("Indice: ", i, "\tValor", v)
    
    
lista= [100, 3.1415, 'Nombre']
print()
for data in lista:
    print(data)

#append(data) -> agrega al final de una lista
#clear () -> borra los elementos de una lista
#copy () -> copia una lista en otra
#count(val) -> cuenta cuantos valores val hay en una lista
#extend(iterable) -> agrega un iterable a una lista( varios valores
#en lugar de append que agrega solo uno)
#index(val) -> retorna el indice donde se encuentra un valor
#insert(index, obj) -> inserta un objeto a partir de un indice en una lista
#pop(index) -> retorna el valor de un indice y lo elimina de una lista
# remove(val) -> elimina un valor de una lista
# reverse() -> invierte el orden de los elementos de una lista
#sort() -> ordena los elementos de una lista de menor a mayor
    
print()
lista=[]
print(lista)
lista.append(10)
#%%
def lista_pares(*args, **kwargs):
    options= args
    keywords= kwargs
    pares=[]
    if len(options) is 2:
        #si hay 2 argumentos, cargalos como 
        #ini y fin (ambos pares)
        fin = options[1]
        if options [0] % 2 is 0:
            ini = options[0]
        else:
            ini= options[0] +1
    elif len(options) is 1:
        #si hay 1 parametro, este sera fin y ini = 0
        ini=0
        fin = options[0]
    
    if keywords.get('endpoint', False):
        fin += 1
    for n in range(ini, fin, 2):
        pares.append(n)
        
    return pares
print(lista_pares(1,10))
print(lista_pares(20))
print(lista_pares(1,10,endpoint=True))


#%%


import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

t = sp.Symbol('t')
x = 0.41 * t**4 - 10.8 * t**3 + 64 * t**2 + 4.4
v = sp.Derivative(x, t).doit()
a = sp.Derivative(x, t, 2).doit()

# sp.lambdify([symbols list], expr, 'numpy')
fx = sp.lambdify([t], x, 'numpy')
fv = sp.lambdify([t], v, 'numpy')
fa = sp.lambdify([t], a, 'numpy')

t = np.linspace(0, 8, 100)
x = fx(t)
v = fv(t)
a = fa(t)

fig = plt.figure(figsize=(6, 8))

plt.subplot(3,1,1)
plt.plot(t, x)
plt.title("Posicion de un particula")
plt.xlabel("Tiempo [seg]")
plt.ylabel("Posicion [ft]")
plt.grid()

plt.subplot(3,1,2)
plt.plot(t, v)
plt.title("Velocidad de un particula")
plt.xlabel("Tiempo [seg]")
plt.ylabel("Posicion [ft/s]")
plt.grid()

plt.subplot(3,1,3)
plt.plot(t, a)
plt.title("Aceleración de un particula")
plt.xlabel("Tiempo [seg]")
plt.ylabel("Aceleración [ft/s^2]")
plt.grid()

plt.tight_layout()
plt.show()


#%%

import numpy as np
import matplotlib.pyplot as plt

R = 80
C = 18e-6
L = 260e-3
vm = 10

fd = np.arange(10, 100000) #paso por defecto =1
wd = 2 * np.pi * fd

I = vm / np.sqrt(R**2 + (wd * L - 1/(wd * C))**2)

plt.figure(figsize=(8, 6))
plt.semilogx(wd, I, color='red') # grafica el semilog de x y es log porque se detalla mejor
plt.title("Corriente en un circuito RLC Serie")
plt.xlabel("Frecuencia [Hz]")
plt.ylabel("Corriente [A]")
plt.grid(linestyle='dashed', which='both') #marca por defecto los grids mayores
plt.show()
#%%
import numpy as np
import matplotlib.pyplot as plt

f = 5
t = np.linspace(0, 1, f * 50)
y = np.cos(2 * np.pi * f * t)

fig = plt.figure(figsize=(8, 6))
fig.set_facecolor('blue')
ax1 = fig.add_subplot(111)

ax1.plot(y, color='green', linewidth=4)
ax1.set_title("Osciloscopio", color='white', fontsize=16)
ax1.set_facecolor('#072d0d')
ax1.set_xticklabels([""])
ax1.set_yticklabels([""])
ax1.grid(True, linestyle='--')

#%%

import numpy as np
import matplotlib.pyplot as plt

f = 5
t = np.linspace(0, 1, f * 50)
y = np.cos(2 * np.pi * f * t)

ang = np.linspace(0, 2* np.pi, 100)
xc = np.cos(ang)
yc = np.sin(ang)

fig = plt.figure(figsize=(16, 6))
fig.set_facecolor('blue')
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)

ax1.plot(y, color='green', linewidth=4)
ax1.set_title("Osciloscopio", color='white', fontsize=16)
ax1.set_facecolor('#072d0d')
ax1.set_xticklabels([""])
ax1.set_yticklabels([""])
ax1.grid(True, linestyle='--')

ax2.plot(xc, yc, color='green', linewidth=4)
ax2.set_title("Osciloscopio", color='white', fontsize=16)
ax2.set_facecolor('#072d0d')
ax2.set_xticklabels([""])
ax2.set_yticklabels([""])
ax2.grid(True, linestyle='--')

#%%

# Libreria Pillow
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

photo = Image.open("model_rgb.jpg")
photo_arr = np.array(photo)

print("Tamaño de la imagen:", photo_arr.shape)
plt.imshow(photo_arr)
plt.tick_params(colors='white')
plt.show()

#%%

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

photo = Image.open("model_rgb.jpg").convert("L")
photo_arr = np.array(photo)

print("Tamaño de la imagen:", photo_arr.shape)
plt.imshow(photo_arr, cmap=cm.Greys_r)
plt.tick_params(colors='white')
plt.show()
#%%

plt.plot([1,2,3,4], [2,31,4,5])
plt.title("Grafica de datos")
plt.ylabel("algunos")
plt.xlabel("sds")

#%%
plt.plot([1,2,3,4], [2,31,4,5], 'g')
plt.axis([0,2,0,20]) #ajusta x de 0 a 2 y Y de 0 a 20
plt.show()

#%%
plt.plot([1,2,3,4], [2,31,4,5], '--g') # linea punteada verde
#plt.axis([0,2,0,20]) #ajusta x de 0 a 2 y Y de 0 a 20
plt.show()

#%%

plt.plot([1,2,3,4], [2,31,4,5], '--go') # linea punteada con picos
#plt.axis([0,2,0,20]) #ajusta x de 0 a 2 y Y de 0 a 20
plt.show()
#%%
plt.plot([1,2,3,4], [2,31,4,5], 'ko') # pone puntos
#plt.axis([0,2,0,20]) #ajusta x de 0 a 2 y Y de 0 a 20
plt.show()
#%%

plt.figure(1)
#grafico rojo
plt.subplot(2,2,1)
plt.plot([1,2,3,4],[1,4,9,16],'b')
plt.axis([0,4,0,20])

#grafico cyan con linea discontinua

plt.subplot(2,2,2)
plt.plot([1,2,3,4],[1,4,9,16],'--c')

#grafico verde con linea discontinua y marcadores redondos

plt.subplot(2,2,3)
plt.plot([1,2,3,4],[1,4,9,16],'--go')

#grafica negro de solo marcadores
#ademas vamos a ajustar los ejes x: 0-6 y: 0-20
plt.subplot(2,2,4)
plt.plot([1,2,3,4],[1,4,9,16],'ko')
plt.axis([0,6,0,20])
plt.show()

#%%
import numpy as np
import matplotlib.pyplot as plt

#un vector con tiempos con intervalos de 200 ms
t=np.arange(0,5,0.2)

#grafico puntos rojos, cuadrados azules y triangulos verdes
plt.plot(t,t, '--r', t, t**2, 'sb',t, t**3, '^g')
plt.legend(["t","t^2","t^3"])
plt.show()

#%%

ang= np.linspace(-2*np.pi, 2*np.pi, 100)
y= np.sin(ang)

#grafica en una sola figura 

plt.figure(1)
plt.plot(ang,y)
plt.title("Funcion seno")
plt.ylabel("Sin(X)")
plt.xlabel("Angulo [rad]")
plt.grid() # hace que haya cuadriculas 

#funcion exponencial
x=np.linspace(-1,1,10)
y=np.exp(x)

#grafica en la primera sub-ventana
plt.figure(2)
plt.title("funcion exponecial")
plt.subplot(2,1,1)
plt.plot(x,y,'r')
plt.ylabel("exp")
plt.grid()

x= np.arange(1,10,0.1)
y=np.log(x+ 10e-20)
#grafica en la 2da subventana
plt.subplot(2,1,2)
plt.plot(x,y,'g')
plt.ylabel("ln")
plt.xlabel("eje x")
plt.grid()
plt.show()
#%%
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

t=sp.Symbol('t')
x=0.41*t**4 - 10.8 * t**3 + 64 * t**2 - 8.2*t + 4.4
v=sp.Derivative(x,t).doit()
a=sp.Derivative(x,t,2).doit()

fx= sp.lambdify([t],x, 'numpy')
fv= sp.lambdify([t],v, 'numpy')
fa= sp.lambdify([t],a, 'numpy')


t=np.linspace(0,12,100)
x=fx(t)
v=fv(t)
a=fa(t)

fig=plt.figure(figsize=(7,11))

plt.subplot(3,1,1)
plt.plot(t,x)
plt.title("Posicion")
plt.grid()

plt.subplot(3,1,2)
plt.plot(t,v)
plt.title("Velocidad")
plt.grid()

plt.subplot(3,1,3)
plt.plot(t,a)
plt.title("Aceleracion")
plt.grid()

plt.show()
#%%

import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

R= 80
C=18e-6
L=260e-3
vm= 10

fd= np.arange(10,10000)
wd=2*np.pi*fd

I=vm / np.sqrt(R**2 + (wd*L - 1 /(wd* C))**2)

plt.figure(figsize=(9,15))
plt.semilogx(wd,I, color='yellow')
plt.title("Ya ps Kenneth")
plt.xlabel("Frecuencia [Hz]")
plt.ylabel("Corriente [A]")
plt.grid()
plt.show()

#%%
import numpy as np
import matplotlib.pyplot as plt

f = 5
t = np.linspace(0, 1, f * 50)
y = np.cos(2 * np.pi * f * t)

fig = plt.figure(figsize=(8, 6))
fig.set_facecolor('blue')
ax1 = fig.add_subplot(111)

ax1.plot(y, color='green', linewidth=4)
ax1.set_title("Osciloscopio", color='white', fontsize=16)
ax1.set_facecolor('#072d0d')
ax1.set_xticklabels([""])
ax1.set_yticklabels([""])
ax1.grid(True, linestyle='--')
#%%
import numpy as np
import matplotlib.pyplot as plt

f = 5
t = np.linspace(0, 1, f * 50)
y = np.cos(2 * np.pi * f * t)

ang = np.linspace(0, 2*np.pi, 100)
xc = np.cos(ang)
yc = np.sin(ang)

fig = plt.figure(figsize=(16, 6))
fig.set_facecolor('blue')
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)

ax1.plot(y, color='green', linewidth=4)
ax1.set_title("Osciloscopio", color='white', fontsize=16)
ax1.set_facecolor('#072d0d')
ax1.set_xticklabels([""])
ax1.set_yticklabels([""])
ax1.grid(True, linestyle='--')

ax2.plot(xc, yc, color='green', linewidth=4)
ax2.set_title("Osciloscopio", color='white', fontsize=16)
ax2.set_facecolor('#072d0d')
ax2.set_xticklabels([""])
ax2.set_yticklabels([""])
ax2.grid(True, linestyle='--')
#%%




#%%

venta= np.array([10,15,14,12,8,12,6,13,12,11,9,14])
mes=np.arange(1,13)
plt.bar(mes,venta)
plt.title("Ventas anuales")
plt.ylabel("Millones")
plt.xlabel("meses")
plt.show()
#%%

#graficas polares

t=np.linspace(0,2*np.pi,200)
r=3*np.cos(0.5*t)**2 + t
plt.polar(t,r)
plt.title("Grafica polar de cos()")
plt.show()
#%%

num= [3,12,8,4]
colors= ['blue','green', 'yellow','red']
explode=[0,0,0,0.2]
plt.pie(num,autopct= '%2.1f%%', explode=explode, colors=colors,shadow= True)
plt.title("Distribucion de notas")
plt.legend(['[20-16]','[15-13]', '[12-8]','[0-8]'],loc='lower left')
plt.show()

#%%

import numpy as np

#datos de entrada
vel=120
ang=np.radians(60)
g=9.81
tvuelo=2*vel*np.sin(ang)/g
#se genera un vector de tiempos
t=np.arange(0,tvuelo,0.1)
x=vel*np.cos(ang)*t
y=vel*np.sin(ang)*t -0.5*g* t**2

plt.plot(x,y)

#formato
plt.title("Grafica de Luis Kepa")
plt.xlabel("distancia en metros")
plt.ylabel("altura")
plt.show()

#%%

import numpy as np
from matplotlib import pyplot as plt

n_dados= int(input("Ingrese el numero de dados a lanzar: "))
n_veces= int(input("Ingrese el numero de lanzamientos: "))

#generar un arreglo de jugadas [n_dados,n_veces] con valores entre
#1 y 6

jugadas=np.random.randint(1,7,(n_dados,n_veces))

#en caso n_dados >1, voy a sumar las caras de los dados
#para saber el resultado de las jugadas

jugadas=np.sum(jugadas,axis=0)

#se genera un arreglo que contenga la distribucion de probabilidad
#se crea un arreglo inicial con P(cara dado)=0
prob=np.array(list([0]*(6* n_dados)))

for i in range(jugadas.size):
    prob[jugadas[i]-1] += 1

prob= prob/ n_veces

#se muestra el grafico con la distribucion de probabilidades
plt.bar(np.arange(1,prob.size+1), prob)
plt.xlim(n_dados -0.5, 6* n_dados +0.5)
plt.title("Distribucion de "+ str(n_dados) + " dado(s)")
plt.xlabel("Resultados")
plt.ylabel("Probabilidad")
plt.show()











#%%

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

photo = Image.open("model_rgb.jpg")
photo_arr = np.array(photo)

photo_R = photo_arr[::,::,0]
photo_G = photo_arr[::,::,1]
photo_B = photo_arr[::,::,2]

fig = plt.figure(figsize=(12, 16))

plt.subplot(141)
plt.imshow(photo_arr)
plt.tick_params(colors='white')
plt.title("Imagen Original")

plt.subplot(142)
plt.imshow(photo_R, cmap=cm.Greys_r)
plt.tick_params(colors='white')
plt.title("Componente R")

plt.subplot(143)
plt.imshow(photo_G, cmap=cm.Greys_r)
plt.tick_params(colors='white')
plt.title("Componente G")

plt.subplot(144)
plt.imshow(photo_B, cmap=cm.Greys_r)
plt.tick_params(colors='white')
plt.title("Componente B")

plt.tight_layout()
plt.show()

#%%
import pyaudio

#Tono de audio digital 440 Hz
ff=440 #frecuencia de 440 HZ
fm=8000 #8000 muestras por segundo
tm= 1/fm #periodo de muestreo
t=3 # señal de 3 s

t_vec =np.arange(0,t,tm)
y=np.sin(2*np.pi*ff*t_vec).astype(np.float32)

#visualizar la onda de audio digital


#Reproducir audio digital
p=pyaudio.PyAudio()

stream=p.open(format=pyaudio.paFloat32,channels=1,rate=8000, output=True)#considera que 1 seg equivale a 8000 muestras
stream.write(y.tostring())
stream.close()
p.terminate()


#%%
#Se genera una señal digital senoidal
import numpy as np
import matplotlib.pyplot as plt

ff = 440      # frecuencia de la señal
fm = 8000     # muestras por segundo
tm = 1 / fm   # Periodo de muestreo
t = 3        # Duracion de la señal a muestrear

#t_vec = np.linspace(0, t, t * fm)
t_vec = np.arange(0, t, tm)
y = np.sin(2 * np.pi * ff * t_vec).astype(np.float32)

fig, ax = plt.subplots(1, figsize=(12, 4))
ax.plot(t_vec, y, '-o', markerfacecolor='k', markersize=5)
ax.set_xlim(0, t/ff)
plt.title(f"Periodo de una señal digital de {ff} Hz")
plt.ylabel("Amplitud")
plt.xlabel("Tiempo [seg]")
plt.grid()
plt.show()

#%%
# Se reproduce la señal digital
import pyaudio

p = pyaudio.PyAudio()

stream = p.open(format=pyaudio.paFloat32, channels=1, rate=8000, output=True)
stream.write(y.tostring())
stream.close()
p.terminate()









