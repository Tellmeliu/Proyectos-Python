# -*- coding: utf-8 -*-
"""
Created on Mon Jun 1 22:35:32 2020

@author: Luis
"""

#%%
import psutil
from tkinter import *
from tkinter import ttk
import tkinter.messagebox
from tkinter.scrolledtext import ScrolledText
from tkinter.messagebox import showinfo, askokcancel
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import datetime

root = Tk()
root.config(bg='black')
root.title("MONITOR PC")

global data_cpu1
data_cpu1=[0]*100
global data_cpu2
data_cpu2=[0]*100
global data_cpu3
data_cpu3=[0]*100


fig = Figure()
fig=Figure(facecolor='black')
ax1=fig.add_subplot(111)

fig2 = Figure()
fig2=Figure(facecolor='black')
ax2=fig2.add_subplot(111)

fig3 = Figure()
fig3=Figure(facecolor='black')
ax3=fig3.add_subplot(111)
#objetos
global cont 
valCPU = DoubleVar(value=0.0)
valMEM= DoubleVar()
valBat = DoubleVar()
cont=0
#funciones
def salir():
    want_to_quit = askokcancel("Salir", "¿Desea salir de la aplicacion?")
    if want_to_quit:
        root.destroy()
def acercaDe():
    showinfo("Acerca de...",
            "Python Notepad 1.0")
def genera_archivo(n):
    global cont
    
    if cont == 0 and n==0:
        
        with open(file='archivo.log', mode='a') as f:
            f.write("Uso del CPU: {:.1f}%".format(valCPU.get()))
            f.write(", ")
            f.write(str(datetime.datetime.now()))
            f.write("\n")
        txtData1.config(bg='#A9A9A9')
        txtData1.config(text="Guardando")
        cont=1
    elif cont == 0 and n==1:
        
        with open(file='archivo.log', mode='a') as f:
            f.write("Uso de la MEM: {:.1f}%".format(valBat.get()))
            f.write(", ")
            f.write(str(datetime.datetime.now()))
            f.write("\n")
        txtData2.config(bg='#A9A9A9')
        txtData2.config(text="Guardando")
        cont=1
    elif cont == 0 and n==2:
        
        with open(file='archivo.log', mode='a') as f:
            f.write("Porcentaje de la Bateria: {:.1f}%".format(valMEM.get()))
            f.write(", ")
            f.write(str(datetime.datetime.now()))
            f.write("\n")
        txtData3.config(bg='#A9A9A9')
        txtData3.config(text="Guardando")
        cont=1
    elif cont==1 and n==0:
        txtData1.config(bg='white')
        txtData1.config(text="LOG DATA")
        cont=0
    elif cont==1 and n==1:
        txtData2.config(bg='white')
        txtData2.config(text="LOG DATA")
        cont=0
    elif cont==1 and n==2:
        txtData3.config(bg='white')
        txtData3.config(text="LOG DATA")
        cont=0
        
def update_graph():
    plotter()
def plotter():
    
    valMEM.set(psutil.virtual_memory().percent)
    barPrincipal_Usage.config(text="{:.1f}%".format(valMEM.get()))
    
    valBat.set(psutil.sensors_battery().percent)
    #valBat_Usage.config(text="{:.1f}%".format(valBat.get()))
    
    valCPU.set(psutil.cpu_percent())
    txtInfo.config(text="MONITOR DE RECURSOS PC", font='Arial 20')

    _ = data_cpu1.pop(0)
    data_cpu1.append(valCPU.get())
    
    ax1.cla() #limpia la grafica
    ax1.grid()
    ax1.set_title("Uso del CPU {}%".format(valCPU.get()), color='white', fontsize=14)
    ax1.plot(data_cpu1,color='green',linewidth=3)
    ax1.tick_params(colors='white')
    ax1.set_facecolor('#072d0d')
    ax1.grid(True, linestyle='--')                  
    ax1.set_ylim(0,100)
    graph.draw()
  
    _ = data_cpu3.pop(0)
    data_cpu3.append(valBat.get())
    
    ax3.cla() #limpia la grafica
    ax3.grid()
    ax3.set_title("Uso de la Bateria {}%".format(valBat.get()), color='white', fontsize=14)
    ax3.plot(data_cpu3,color='green',linewidth=3)
    ax3.tick_params(colors='white')
    ax3.set_facecolor('#072d0d')
    ax3.grid(True, linestyle='--')
    ax3.set_ylim(0,100)
    graph3.draw()
    
    root.after(100, update_graph)
#frames
main_menu = Menu(root)
root.configure(menu=main_menu)

menu_archivo = Menu(main_menu, tearoff=False)
menu_ayuda = Menu(main_menu, tearoff=False)

menu_archivo.add_command(label="Salir", command=salir)

menu_ayuda.add_command(label="Acerca de...",  command=acercaDe)

main_menu.add_cascade(label="Archivo", menu=menu_archivo)
main_menu.add_cascade(label="Ayuda", menu=menu_ayuda)

frmC=Frame(root)
frm1=Frame(root)
frm2=Frame(root)
frm3=Frame(root)
frm1in = Frame(frm1)
frm2in = Frame(frm2)
frm3in = Frame(frm3)
frmC.config(bg='black')
frm1.config(bg='black')
frm2.config(bg='black')
frm3.config(bg='black')
frm1in.config(bg='black')
frm2in.config(bg='black')
frm3in.config(bg='black')
frmC.pack(side=TOP, expand=YES)
frm1.pack(side=LEFT,expand=YES)
frm2.pack(side=LEFT, expand=YES)
frm3.pack(side=LEFT, expand=YES)
frm1in.grid()
frm2in.grid()
frm3in.grid()

graph=FigureCanvasTkAgg(fig,master=frm1in)
graph.get_tk_widget().pack(expand=True,fill='x')

graph3=FigureCanvasTkAgg(fig3,master=frm3in)
graph3.get_tk_widget().pack(expand=True,fill='x')
txtInfo=Label(frmC, text="MONITOR DE RECURSOS PC", bg='black', fg='white', font= 'Arial')
txtInfo2=Label(frmC, text="Velocidad del CPU: \t\t\t{:.2f} GHz".format(psutil.cpu_freq().current),bg='black', fg='white', font='Arial')
txtInfo3=Label(frmC, text="Total de memoria(RAM): \t\t{:.2F} GB".format(psutil.virtual_memory().total/1e9),bg='black', fg='white', font='Arial')
txtInfo4=Label(frmC, text="Disco Local (C:): (Espacio Total): \t{:.2f} GB".format(psutil.disk_usage('C:\\').total/1e9),bg='black', fg='white', font='Arial')
txtInfo5=Label(frmC, text="Disco Local (C:): (Espacio disponible): \t{:.2f} GB".format(psutil.disk_usage('C:\\').free/1e9),bg='black', fg='white', font='Arial')
txtInfo6=Label(frmC, text="Disco Local (D:): (Espacio Total): \t{:.2f} GB".format(psutil.disk_usage('D:\\').total/1e9),bg='black', fg='white', font='Arial')
txtInfo7=Label(frmC, text="Disco Local (D:): (Espacio disponible): \t{:.2f} GB".format(psutil.disk_usage('D:\\').free/1e9),bg='black', fg='white', font='Arial')
txtData1=Button(frm1, text="LOG DATA", command=lambda: genera_archivo(0), bg = "white")
txtData2=Button(frm2, text="LOG DATA", command=lambda: genera_archivo(1), bg = "white")
txtData3=Button(frm3, text="LOG DATA", command=lambda: genera_archivo(2), bg = "white")
barPrincipal=Label(frm2in,text="Memoria RAM", bg='black', fg='white', font= 'Arial')
barPrincipal_Usage = Label(frm2in, text="{:.1f}%".format(valMEM.get()), bg='black', fg = 'white')


barMEM = ttk.Progressbar(frm2in, orient= VERTICAL, length=250, variable=valMEM)
barMEM1 = ttk.Progressbar(frm2in, orient= VERTICAL, length=250, variable=valMEM)
barMEM2= ttk.Progressbar(frm2in, orient= VERTICAL, length=250, variable=valMEM)
barMEM3= ttk.Progressbar(frm2in, orient= VERTICAL, length=250, variable=valMEM)
barMEM4= ttk.Progressbar(frm2in, orient= VERTICAL, length=250, variable=valMEM)
barMEM5= ttk.Progressbar(frm2in, orient= VERTICAL, length=250, variable=valMEM)
barMEM6= ttk.Progressbar(frm2in, orient= VERTICAL, length=250, variable=valMEM)
barMEM7= ttk.Progressbar(frm2in, orient= VERTICAL, length=250, variable=valMEM)

txtInfo.grid(sticky=W)
txtInfo2.grid(sticky=W)
txtInfo3.grid(sticky=W)
txtInfo4.grid(sticky=W)
txtInfo5.grid(sticky=W)
txtInfo6.grid(sticky=W)
txtInfo7.grid(sticky=W)
txtData1.grid(row=4 , column=0, sticky=W, padx=180)
txtData2.grid(row=4 , column=0, sticky=W, padx=180)
txtData3.grid(row=4 , column=0, sticky=W, padx=180)

barPrincipal.grid(row=0, column=0, columnspan=5)
barPrincipal_Usage.grid(row=0,column=6,columnspan=2,sticky='e')
barMEM.grid(row=2, column=0)#, columnspan=2)
barMEM1.grid(row=2, column=1)
barMEM2.grid(row=2, column=2)
barMEM3.grid(row=2, column=3)
barMEM4.grid(row=2, column=4)
barMEM5.grid(row=2, column=5)
barMEM6.grid(row=2, column=6)
barMEM7.grid(row=2, column=7)

#binds
root.after(100, update_graph)


root.mainloop()

