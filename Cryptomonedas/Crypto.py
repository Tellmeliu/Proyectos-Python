# -*- coding: utf-8 -*-
"""
Created on Fri May 15 07:11:32 2020

@author: Luis
"""

#%%
import pandas as pd
from tkinter import *
import tkinter.ttk as ttk
from tkinter import Tk,Label
from tkcalendar import DateEntry
from datetime import datetime,timedelta
from tkinter.ttk import Notebook,Combobox
from random import randint
from bs4 import BeautifulSoup
import requests
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np

#LECTURA DE API
url = "https://api.coinbase.com/v2/prices/BTC-USD/spot"
r = requests.get(url)
data_dic = r.json()
data= data_dic['data']
print(data['amount'])

url2 = "https://api.coinbase.com/v2/prices/ETH-USD/spot"
r2 = requests.get(url2)
data_dic2 = r2.json()
data2= data_dic2['data']
print(data2['amount'])



class Tabla:
    def __init__(self,master):
        self.master=master
        self.master.title("Crypto Monitor")
        self.master.config(bg='white')
        
        self.fig = Figure(figsize=(5,5))
        self.ax1= self.fig.add_subplot(111)
        self.t=np.arange(-1.1,1.1,0.01)
        
        #Beautifulsoup
        
        self.url = "https://coinmarketcap.com/currencies/bitcoin/"        
        self.r = requests.get(self.url)
        
        self.soup = BeautifulSoup(self.r.text, 'lxml')
        
        self.bitcoin = self.soup.find('div',class_="col-sm-8")
        #print(self.bitcoin.text)
        
        self.url2 = "https://coinmarketcap.com/currencies/ethereum/"
        self.r2 = requests.get(self.url2)

        self.soup2 = BeautifulSoup(self.r2.text, 'lxml')

        self.ethereum = self.soup2.find('div',class_="col-sm-8")
        #print(self.ethereum.text)
        
        self.url3 = "https://coinmarketcap.com/currencies/litecoin/"
        self.r3 = requests.get(self.url3)

        self.soup3 = BeautifulSoup(self.r3.text, 'lxml')

        self.linecoin = self.soup3.find('div',class_="col-sm-8")
        #print(self.linecoin.text)
        
        self.url4 = "https://coinmarketcap.com/currencies/bitcoin-cash/"
        self.r4 = requests.get(self.url4)

        self.soup4 = BeautifulSoup(self.r4.text, 'lxml')

        self.cash = self.soup4.find('div',class_="col-sm-8")
        #print(self.cash.text)
        
        #calculo para que inicie en los ultimos 7 dias los calendarios
        fecha = datetime.now()
        ano_7 = IntVar()
        ano_7.set(fecha.year)
        mes_7 = IntVar()
        dia_7 = IntVar()
        if dia_7.get()>7:
            mes_7.set(fecha.month)
            dia_7.set(fecha.day-7)
        else:
            mes_7.set(fecha.month-1)
            dia_7.set((fecha.day+31)-7)
            
        
        #objetos
        self.master=master
        self.c_token=["Bitcoin","Ethereum","Litecoin","Bitcoin Cash"]
        self.USD = StringVar()
        self.USD.set("0.0")
        self.color=StringVar()
        self.color.set('red')
        self.master.resizable(0, 0)
        self.texto =StringVar()
        self.texto.set("Seleccione una cripto...")
        self.color_plot = StringVar()
       
        #frames
        
        frm = Frame(root)
        frmToken = LabelFrame(frm,foreground='black', text="Token")
        frmFecha = LabelFrame(frm,foreground='black', text="Rango Fecha")
        frmTabla = LabelFrame(frm,foreground='black', text="Tablas y Gráficos")
        frm.pack()
        frmToken.pack()
        frmFecha.pack()
        frmTabla.pack()
        
        self.cmbToken = ttk.Combobox(frmToken,values=self.c_token, textvariable=self.texto)
        self.lblUSD = Label(frmToken, text="{} USB".format(self.USD.get()),fg='red', font= 'Arial')
        self.date_entry=DateEntry(frmFecha, day=dia_7.get(), month=mes_7.get(), year=ano_7.get())
        self.date_entry2=DateEntry(frmFecha)
        self.bonAsignar = Button(frmFecha, text="Asignar", command=self.asignar)
        self.notebook=Notebook(frmTabla)
        self.notebook.pack(padx=10,pady=10)
        self.cmbToken.grid(row=0, column=0,sticky=W, padx=25)
        self.lblUSD.grid(row=0, column=1,sticky=W, padx=25)
        self.date_entry.grid(row=0,column=0,sticky=W, padx=12,pady=5)
        self.date_entry2.grid(row=0,column=1,sticky=W, padx=12,pady=5)
        self.bonAsignar.grid(row=0,column=2,sticky=W, padx=12,pady=5)
        
       
        self.info= Text(self.notebook, height=25, width=30)
        self.tabla=LabelFrame(self.notebook,text="Seleccione un color")
        self.grafico=LabelFrame(self.notebook,text="Grafico")
        self.combobox=Combobox(self.tabla,values=['red','blue','green','black','pink'],textvariable=self.color,justify='left')
        self.combobox.grid(row=0,column=0,padx=5,pady=5,sticky='w')
        self.info.insert(END, "\n" )
        self.notebook.add(self.info,text="Info",padding=30)
        self.notebook.add(self.tabla,text="Tabla",padding=30)
        self.notebook.add(self.grafico,text="Gráfico",padding=30)
        self.graph=FigureCanvasTkAgg(self.fig,master=self.grafico)
        self.graph.get_tk_widget().pack(expand=True,fill='x')
        self.date=self.date_entry.get_date()
        self.date2=self.date_entry2.get_date()
        
        #binds
        self.graph.draw()
        self.date_entry.bind("<<DateEntrySelected>>",self.print_date)
        self.date_entry2.bind("<<DateEntrySelected>>",self.print_date)
        self.cmbToken.bind("<<ComboboxSelected>>", self.cambia_combo)
        
    def asignar(self):
        self.ax1.cla()
        auxi=self.btc_df.loc[self.date2:self.date]['Close**']
        self.ax1.plot(auxi, color=self.color_plot.get())
        self.ax1.set_xlabel('Día')
        self.graph.draw()
        
    def print_date(self,handle):
        self.date=self.date_entry.get_date()
        self.date2=self.date_entry2.get_date()
        self.date=str(self.date)
        self.date2=str(self.date2)        
        
    def cambia_combo(self,event):
        if "Bitcoin"==self.texto.get():
            self.lblUSD.config(text="{} USB".format(data["amount"]))
            self.info.delete(1.0, END)
            self.info.insert(END, self.bitcoin.text )
            self.ax1.cla()
            self.url_extra= "https://coinmarketcap.com/currencies/bitcoin/historical-data/?start=20130428&end=20190527"
            self.rango = pd.read_html(self.url_extra)
            self.btc_df = self.rango[0]
            self.btc_df.set_index(pd.DatetimeIndex(self.btc_df['Date']), inplace=True)
            auxi=self.btc_df.loc[self.date2:self.date]['Close**']
            self.color_plot.set('blue')
            self.ax1.plot(auxi, color=self.color_plot.get())
            self.ax1.set_xlabel('Día')
            self.graph.draw()
            
        elif "Ethereum"==self.texto.get():
            self.lblUSD.config(text="{} USB".format(data2["amount"]))
            self.info.delete(1.0, END)
            self.info.insert(END, self.ethereum.text )
            self.ax1.cla()
            self.url_extra= "https://coinmarketcap.com/currencies/ethereum/historical-data/?start=20130428&end=20190601"
            self.rango = pd.read_html(self.url_extra)
            self.btc_df = self.rango[0]
            self.btc_df.set_index(pd.DatetimeIndex(self.btc_df['Date']), inplace=True)
            auxi=self.btc_df.loc[self.date2:self.date]['Close**']
            self.color_plot.set('black')
            self.ax1.plot(auxi, color=self.color_plot.get())
            self.ax1.set_xlabel('Día')
            self.graph.draw()
            
        elif "Litecoin"==self.texto.get():
            self.info.delete(1.0, END)
            self.info.insert(END, self.linecoin.text )
            self.ax1.cla()
            self.url_extra= "https://coinmarketcap.com/currencies/litecoin/historical-data/?start=20130428&end=20190601"
            self.rango = pd.read_html(self.url_extra)
            self.btc_df = self.rango[0]
            self.btc_df.set_index(pd.DatetimeIndex(self.btc_df['Date']), inplace=True)
            auxi=self.btc_df.loc[self.date2:self.date]['Close**']
            self.color_plot.set('red')
            self.ax1.plot(auxi, color=self.color_plot.get())
            self.ax1.set_xlabel('Día')
            self.graph.draw()
        elif "Bitcoin Cash"==self.texto.get():
            self.info.delete(1.0, END)
            self.info.insert(END, self.cash.text )
            self.ax1.cla()
            self.url_extra= "https://coinmarketcap.com/currencies/bitcoin-cash/historical-data/?start=20130428&end=20190601"
            self.rango = pd.read_html(self.url_extra)
            self.btc_df = self.rango[0]
            self.btc_df.set_index(pd.DatetimeIndex(self.btc_df['Date']), inplace=True)
            auxi=self.btc_df.loc[self.date2:self.date]['Close**']
            self.color_plot.set('green')
            self.ax1.plot(auxi,color=self.color_plot.get())
            self.ax1.set_xlabel('Día')
            self.graph.draw()
 
root = Tk()
app = Tabla(root)
root.mainloop()