# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 18:45:13 2020

@author: Luis
"""

#%%
from tkinter import *
from tkinter import ttk

class Calculator():
    def __init__(self, master):
        self.calc_value = 0.0
        
        self.add_op = BooleanVar(value=False)
        self.sub_op = BooleanVar(value=False)
        self.mul_op = BooleanVar(value=False)
        self.div_op = BooleanVar(value=False)
        
        # Propiedades de la ventana
        master.title("Calculadora")
        master.resizable(0, 0)

        # Marco de la calculadora
        frame = Frame(master)
        frame.pack()

        # Menu
        self.menu = Menu(master)
        master.config(menu=self.menu)
        
        self.menu.add_command(label="Reset", command=self.resetEntry)
        
        # Variables de las propiedades (Fields)
        self.num = StringVar(value="")
        
        # Widgets
        self.num_entry = ttk.Entry(frame, textvariable=self.num, font="Arial 20 bold", justify='right')
        self.button0 = ttk.Button(frame, text='0', command=lambda: self.button_press('0'))
        self.button1 = ttk.Button(frame, text='1', command=lambda: self.button_press('1'))
        self.button2 = ttk.Button(frame, text='2', command=lambda: self.button_press('2'))
        self.button3 = ttk.Button(frame, text='3', command=lambda: self.button_press('3'))
        self.button4 = ttk.Button(frame, text='4', command=lambda: self.button_press('4'))
        self.button5 = ttk.Button(frame, text='5', command=lambda: self.button_press('5'))
        self.button6 = ttk.Button(frame, text='6', command=lambda: self.button_press('6'))
        self.button7 = ttk.Button(frame, text='7', command=lambda: self.button_press('7'))
        self.button8 = ttk.Button(frame, text='8', command=lambda: self.button_press('8'))
        self.button9 = ttk.Button(frame, text='9', command=lambda: self.button_press('9'))
        self.button_add = ttk.Button(frame, text='+', command=self.pressAdd)
        self.button_sub = ttk.Button(frame, text='-', command=self.pressSub)
        self.button_mul = ttk.Button(frame, text='x', command=self.pressMul)
        self.button_div = ttk.Button(frame, text='/', command=self.pressDiv)
        self.button_point = ttk.Button(frame, text='.', command=lambda: self.button_press('.'))
        self.button_equal = ttk.Button(frame, text='=', command=self.equal)
        self.button_del = ttk.Button(frame, text='DEL')
     
        # Colocacion de los widgets
        self.num_entry.grid(row=0, column=0, columnspan=4)
        self.button7.grid(row=1, column=0)
        self.button8.grid(row=1, column=1)
        self.button9.grid(row=1, column=2)
        self.button_div.grid(row=1, column=3)
        self.button4.grid(row=2, column=0)
        self.button5.grid(row=2, column=1)
        self.button6.grid(row=2, column=2)
        self.button_mul.grid(row=2, column=3)
        self.button1.grid(row=3, column=0)
        self.button2.grid(row=3, column=1)
        self.button3.grid(row=3, column=2)
        self.button_sub.grid(row=3, column=3)
        self.button_point.grid(row=4, column=0)
        self.button0.grid(row=4, column=1)
        self.button_equal.grid(row=4, column=2)
        self.button_add.grid(row=4, column=3)

    def pressAdd(self):
        if len(self.num.get()) == 0 and self.calc_value != 0.0:
            pass
        else:
            self.add_op.set(True)
            self.sub_op.set(False)
            self.mul_op.set(False)
            self.div_op.set(False)
            self.calc_value = float(self.num.get())
            self.num.set('')
            
    def pressSub(self):
        if len(self.num.get()) == 0 and self.calc_value != 0.0:
            pass
        else:
            self.add_op.set(False)
            self.sub_op.set(True)
            self.mul_op.set(False)
            self.div_op.set(False)
            self.calc_value = float(self.num.get())
            self.num.set('')
        
    def pressMul(self):
        if len(self.num.get()) == 0 and self.calc_value != 0.0:
            pass
        else:
            self.add_op.set(False)
            self.sub_op.set(False)
            self.mul_op.set(True)
            self.div_op.set(False)
            self.calc_value = float(self.num.get())
            self.num.set('')
        
    def pressDiv(self):
        if len(self.num.get()) == 0 and self.calc_value != 0.0:
            pass
        else:
            self.add_op.set(False)
            self.sub_op.set(False)
            self.mul_op.set(False)
            self.div_op.set(True)
            self.calc_value = float(self.num.get())
            self.num.set('')
            
    def button_press(self, number):
        if number == '0' or number == "." and len(self.num.get()) == 0:
            pass
        else:
            self.num.set(self.num.get() + number)
    
    def equal(self):        
        if self.add_op.get() == True:
            self.calc_value += float(self.num.get())
            self.num.set(str(self.calc_value))
            self.calc_value = 0.0
            self.add_op.set(False)
        elif self.sub_op.get() == True:
            self.calc_value -= float(self.num.get())
            self.num.set(str(self.calc_value))
            self.calc_value = 0.0
            self.sub_op.set(False)
        elif self.mul_op.get() == True:
            self.calc_value *= float(self.num.get())
            self.num.set(str(self.calc_value))
            self.calc_value = 0.0
            self.mul_op.set(False)
        elif self.div_op.get() == True:
            self.calc_value /= float(self.num.get())
            self.num.set(str(self.calc_value)) 
            self.calc_value = 0.0
            self.div_op.set(False)
        
        
    def resetEntry(self):
        self.num.set('')
        
def main():
	root = Tk()
	app = Calculator(root)
	root.mainloop()

if __name__ == '__main__':
	main()
