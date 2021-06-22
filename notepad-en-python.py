# -*- coding: utf-8 -*-
"""
Created on Sun May 23 23:57:21 2020

@author: Luis
"""

#%%


#%%

import os
from tkinter import *
from tkinter.scrolledtext import ScrolledText
from tkinter.messagebox import showinfo, askokcancel
from tkinter.filedialog import askopenfilename, asksaveasfilename, asksaveasfile

# Funciones
def nuevoArchivo():
    global file
    root.title("Sin Titulo - Notepad")
    file = None
    text_area.delete(1.0, END)

def abrirArchivo():
    global file
    file = askopenfilename(defaultextension=".txt",
                          filetypes=[("Todos los archivos", "*.*"),
                                    ("Archivos de texto", "*.txt")])
    if file is "":
        file = None
    else: 
        root.title(os.path.basename(file) + " - Notepad")
        text_area.delete(1.0, END)
        f = open(file, 'r')
        text_area.insert(1.0, f.read())
        f.close()
        
def guardarArchivo():
    global file
    if file is None:
        guardarComo()
    else:
        f = open(file, 'w')
        f.write(text_area.get(1.0, END))
        f.close()
        
def guardarComo():
    global file
    file = asksaveasfilename(filetypes=[("Todos los archivos", "*.*"),
                                        ("Archivos de texto", "*.txt")])

    if file is "":
        file = None
    else:
        f = open(file, 'w')
        f.write(text_area.get(1.0, END))
        f.close()

        root.title(os.path.basename(file) + " - Notepad")

def cortar():
    text_area.event_generate(("<Cut>"))

def copiar():
    text_area.event_generate(("<Copy>"))

def pegar():
    text_area.event_generate(("<Paste>"))

def salir():
    want_to_quit = askokcancel("Salir", "¿Desea salir de la aplicacion?")
    if want_to_quit:
        root.destroy()

def acercaDe():
    showinfo("Acerca de...",
            "Python Notepad 1.0")

def printStatusBar(widget):
    fil, col = widget.index(INSERT).split(".")
    status_bar.config(text="FIL: {:3}  COL: {:3}".format(fil, col))
        
# Ventana root
root = Tk()
root.title("Sin Titulo - Notepad")
file = None

# Frames
frm = Frame(root)
frm.pack(expand=True, fill=BOTH)

# Menu
main_menu = Menu(root)
root.configure(menu=main_menu)

menu_archivo = Menu(main_menu, tearoff=False)
menu_editar = Menu(main_menu, tearoff=False)
menu_ayuda = Menu(main_menu, tearoff=False)

menu_archivo.add_command(label="Nuevo", command=nuevoArchivo)
menu_archivo.add_command(label="Abrir", command=abrirArchivo)
menu_archivo.add_command(label="Guardar", command=guardarArchivo)
menu_archivo.add_command(label="Guardar como...", command=guardarComo)
menu_archivo.add_separator()
menu_archivo.add_command(label="Salir", command=salir)

menu_editar.add_command(label="Cortar", accelerator="Ctrl+X", command=cortar)
menu_editar.add_command(label="Copiar", accelerator="Ctrl+C", command=copiar)
menu_editar.add_command(label="Pegar", accelerator="Ctrl+V", command=pegar)

menu_ayuda.add_command(label="Acerca de...", command=acercaDe)

main_menu.add_cascade(label="Archivo", menu=menu_archivo)
main_menu.add_cascade(label="Editar", menu=menu_editar)
main_menu.add_cascade(label="Ayuda", menu=menu_ayuda)

# Widgets y GM
text_area = ScrolledText(frm)
text_area.pack(expand=True, fill=BOTH)

# Status Bar
status_bar = Label(root, text="Listo", bd=1, relief=SUNKEN, anchor=W)
status_bar.pack(side=BOTTOM, expand=True, fill=X)

# Binds
text_area.bind("<KeyPress>", lambda x: printStatusBar(text_area))
text_area.bind("<Left>", lambda x: printStatusBar(text_area))
text_area.bind("<Right>", lambda x: printStatusBar(text_area))
text_area.bind("<Up>", lambda x: printStatusBar(text_area))
text_area.bind("<Down>", lambda x: printStatusBar(text_area))
#TODO: Fix Enter to Newline !!!

root.mainloop()


