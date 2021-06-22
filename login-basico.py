

#%%
#TKINTER
from tkinter import *
root= Tk()
root.title("User Login")
root.resizable(0,0)
#root.geometry("200x200+100+100")

# Obj- Var 
user = StringVar()
password=StringVar()
remember= BooleanVar() 

try:
    f= open("login.tmp")
    user.set(f.read().strip())# elimina strip tabs, etc
    if len(user.get()) > 0:
        remember.set(True)
        
    f.close()
except:
    pass    
    
    
#funciones

#def print_login():
#    print(user.get())
def login_button():
    f= open("login.tmp",mode='w')
    
    if remember.get():
        f.write(user.get())
    else:
        f.write("")
        
    f.close()
    user.set("")
    password.set("")
    entUser.focus()
    


#frames + pack 
frm1= Frame(root)
frm2= Frame(root)
frm3= Frame(root)

frm1.pack(padx=10,pady=10)
frm2.pack(padx=10)
frm3.pack(padx=10,pady=10)

#widgets + grid <pack, place>
#--------------------frm1-------------------------
lblUser = Label(frm1, text= "User: ",font='Arial 12 bold')
lblPassword= Label(frm1, text= "Password: ")
entUser= Entry(frm1, textvariable=user)
entPassword = Entry(frm1,show='*',textvariable=password)#show hace que se vea los asteriscos

lblUser.grid(row=0 , column=0 , padx= 5 , pady=5,sticky=E)
lblPassword.grid(row=1 , column=0 , padx= 5 , pady=5, sticky=E)
entUser.grid(row=0 , column=1 , padx= 5 , pady=5)
entPassword.grid(row=1 , column=1 , padx= 5 , pady=5)
#sticky esta pegado
entUser.focus()
#--------------------frm2-------------------------

chkRemember= Checkbutton(frm2,text="Recuerdame?",variable=remember)
chkRemember.grid(row=0 , column=0 , padx= 5 , pady=5)

#--------------------frm3-------------------------
btnLogin= Button(frm3,text="Login",width=12,command=login_button)
btnQuit= Button(frm3,text="Quit",width=12,command=root.destroy)
btnLogin.grid(row=0 , column=0 , padx= 5 , pady=5)
btnQuit.grid(row=0 , column=1 , padx= 5 , pady=5)

root.mainloop() # hace sacar una ventanita


#%%
#TKINTER
from tkinter import *
from tkinter import ttk

root= Tk()
#root
root.title("Quiosco pasajero")
root.resizable(0,0)

#obj var
precio= DoubleVar()

#funciones


#frames
frm= Frame(root,borderwidth=2,relief=GROOVE)
frm1= Frame(frm)
frm2= Frame(frm)
frm3= Frame(frm)
frm4= Frame(frm)

frm.pack(padx= 10 , pady=10)
frm1.pack(padx= 10 , pady=10)
frm2.pack(padx= 10 , pady=10)
frm3.pack(padx= 10 , pady=10)
frm4.pack(padx= 10 , pady=10)
#widgets


#-------frm1----------

img = PhotoImage(file= "tren.png",format='png')
lblTren= Label(frm1,image=img)
lblTren.grid(row=0,column=0,padx=5,pady=5)


#-------frm2----------

lblDestinos= ttk.Label(frm2, text="Destinos")
cboDestinos= ttk.Combobox(frm2)
lblPrecio= ttk.Label(frm2, text="Precio {:5.2f}".format(precio.get()))
lblNumTickets= ttk.Label(frm2,text="Num tickets")
entNumTickets= ttk.Entry(frm2,width=8)

lblDestinos.grid(row=0 , column=0 , padx= 5 , pady=5,sticky=W)
cboDestinos.grid(row=1 , column=0 ,columnspan=2, padx= 5 , pady=5)
lblPrecio.grid(row=2 , column=0 , padx= 5 , pady=5,sticky=W)
lblNumTickets.grid(row=3 , column=0 , padx= 5 , pady=5)
entNumTickets.grid(row=3 , column=1 , padx= 5 , pady=5)

#--------frm3----------

rdoSoloIda=ttk.Radiobutton(frm3,text="Solo Ida")
rdoIdaVuelta =ttk.Radiobutton(frm3,text="Ida Y Vuelta")
lblPrecioTotal=ttk.Label(frm3,text="Precio {:5.2f}".format(precio.get(), font='Time 12 bold')


rdoSoloida.grid(row=0 , column=0 , padx= 5 , pady=5,sticky=W)
rdoIdaVuelta.grid(row=1 , column=0 , padx= 5 , pady=5,sticky=W)
#---------frm4----------


root.mainloop() 