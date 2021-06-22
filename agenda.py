#%%
# -*- coding: utf-8
import os
import time
import datetime
import json

'''
Diccionario de contacto
=======================

data = {
        contactos: [
                      {
                      'nombre': None,
                      'apellido': None,
                      'telefono': {
                                  'fijo': None,
                                  'movil': None,
                                  },
                      'email': {
                                'personal': None,
                                'trabajo': None, 
                               }
                      'fecha_nac': None,
                     },
                ]
       }
'''

class Contacto:
    def __init__(self, nombre, apellido, t_fijo, t_movil, email_per, email_lab, fecha_nac):
        self.nombre = nombre
        self.apellido = apellido
        self.t_fijo = t_fijo
        self.t_movil = t_movil
        self.email_per = email_per
        self.email_lab = email_lab
        self.fecha_nac = fecha_nac
        self.edad = self.__set_edad()
    
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, val):
        if isinstance(val, str):
            self.__nombre = val
        else:
            raise TypeError("El campo 'nombre' debe ser un 'str'")

    def __set_edad(self):
        
        dia1, mes1,ano1 = self.fecha_nac.split('/')
        dia1=int(dia1)
        mes1=int(mes1)
        ano1=int(ano1)
    
        hoy = datetime.datetime.now()
         
        fecha_nac1 = datetime.datetime(ano1, mes1, dia1, 0, 0, 0)
    
        delta_tiempo = hoy - fecha_nac1 #edad en dias
        edad = delta_tiempo//365
        return str(edad.days)
        
    
    def __repr__(self):
        str_out = 'Contacto:\n'
        str_out += '\tNombre: {}\n'.format(self.nombre)
        str_out += '\tApellido: {}\n'.format(self.apellido)
        str_out += '\tTelefono fijo: {}\n'.format(self.t_fijo)
        str_out += '\tTelefono movil: {}\n'.format(self.t_movil)
        str_out += '\tEmail personal: {}\n'.format(self.email_per)
        str_out += '\tEmail trabajo: {}\n'.format(self.email_lab)
        str_out += '\tFecha nac: {}\n'.format(self.fecha_nac)
        str_out += '\tEdad: {} años\n'.format(self.edad)
        return str_out

    

def clear_screen():
    _ = os.system('cls')
    return None


def show_menu():
    clear_screen()
    print("\nAGENDA DE CONTACTOS")
    print("====================")
    print("[1] Agregar contacto")
    print("[2] Mostrar contactos")
    print("[3] Ver detalle de contactos")
    print("[4] Editar contacto")
    print("[5] Borrar contacto")
    print("[0] Salir")
    opc = int(input("\nOpcion: "))
    
    return opc


def read_file(contact_list):
    '''
    Esta funcion lee un archivo json con la informacion de los contactos
    registrados y retorna una lista con objetos Contacto
    '''
    with open("contactos.json") as json_file:
        contact_dic={}
        contact_dic = json.load(json_file)
        contact_list = contact_dic['contactos']
    
    lista_cont = []
    for idx in range (0,len(contact_list)):
        
        lista_cont.append(Contacto(nombre=contact_list[idx]['nombre'], 
                                   apellido=contact_list[idx]['apellido'],
                                   t_fijo=contact_list[idx]['telefono']['fijo'],
                                   t_movil=contact_list[idx]['telefono']['movil'],
                                   email_per=contact_list[idx]['email']['personal'],
                                   email_lab=contact_list[idx]['email']['trabajo'],
                                   fecha_nac=contact_list[idx]['fecha_nac']))
        
                                   
                                   
                                   
    return lista_cont


def write_file(file, contact_list):#documento,clase
    '''
    Esta funcion crear un diccionario con la informacion de la lista de 
    contactos (con objetos Contacto) y escribe un archivo json con la
    informacion del diccionario
    '''
    data = dict(contactos=[])
    
    for i in range (0,len(contact_list)):
        
        data['contactos'].append({'nombre': contact_list[i].nombre,
                            'apellido': contact_list[i].apellido,
                            'telefono':{'fijo': contact_list[i].t_fijo,'movil': contact_list[i].t_movil},
                            'email':{'personal':contact_list[i].email_per ,'trabajo':contact_list[i].email_lab},
                            'fecha_nac':contact_list[i].fecha_nac
                           })
    
    with open(file, mode='w') as json_file:
        json.dump(data, json_file)
        
    return None  
    
    
    

def find_contact(contact_list, name_str): #clase,str
    '''
    Esta funcion busca en una lista de contactos (con objetos Contactos)
    un contacto especificado por nombre
    '''
    for i in range(0, len(contact_list)):
        if name_str.lower() == contact_list[i].nombre.lower():
            encontrado = contact_list[i]
            break
        
        elif name_str.lower() == contact_list[i].apellido.lower():
            encontrado = contact_list[i]
            break
        
        else:
            encontrado = None
            
    return encontrado

def edit_contact(contact_obj,campo):
    '''
    Funcion que cambia los cambios de un objeto Contacto
    '''
    if campo == 'nombre':
        contact_obj.nombre = input("Nombre[{}]: ".format(contact_obj.nombre))
    elif campo == 'apellido':
        contact_obj.apellido = input("Apellido[{}]: ".format(contact_obj.apellido))
    elif campo == 'telefono fijo':
        contact_obj.t_fijo = input("telefono fijo[{}]: ".format(contact_obj.t_fijo))
    elif campo == 'telefono movil':
        contact_obj.t_movil = input("telefono movil[{}]: ".format(contact_obj.t_movil))
    elif campo == 'email personal':
        contact_obj.email_per = input("Email personal[{}]: ".format(contact_obj.email_per))
    elif campo == 'email trabajo':
        contact_obj.email_lab = input("Email trabajo[{}]: ".format(contact_obj.email_lab))
    elif campo == 'fecha nac':
        contact_obj.fecha_nac = input("Fecha nac[{}]: ".format(contact_obj.fecha_nac))
    
    
    return contact_obj


def delete_contact(lista_completa, contact_list):
    '''
    Funcion que elimina un objeto Contacto de una lista de objetos Contactos
    '''
    indice = lista_completa.index(contact_list)
    lista_completa.pop(indice)
    
    write_file('contactos.json',lista_completa)
    
    return None
    


def show_contact(contact):
    '''
    Funcion que muestra los detalles de un objeto Contacto <print(obj)>
    '''
    if contact == None:
        print("No se ha encontrado el contacto")
    else: 
       
        print(contact)
    return None 


def list_contact(contact_list):#jala un objeto contacto
    '''
    Funcion que muestra un listado de contactos numerados con la informacion
    de nombre y apellido en ordenado de forma alfabetica
    '''
    seleccion=[]
    lista_orden=[]
    numeros=[]
    for i in range(0,len(contact_list)):
        val=contact_list[i].nombre[0]
        numeros.append(val)
        seleccion.append(0)
    numeros.sort()
    for i in range(0,len(contact_list)):
        for j in range(0,len(contact_list)):
            if numeros[i]==contact_list[j].nombre[0]:
                if seleccion[j]==0:
                    lista_orden.append(contact_list[j])
                    seleccion[j]=1
            else:
                pass
    for i in range(0,len(lista_orden)):
        for j in range(1,len(lista_orden)):
            if lista_orden[i].nombre[0]==lista_orden[j].nombre[0]:
                if lista_orden[i].nombre[1]<lista_orden[j].nombre[1]:
                    aux1=lista_orden[i]
                    aux2=lista_orden[j]
                    #aux2=contact_list.pop(i)
                    lista_orden[i]=aux2
                    lista_orden[j]=aux1
                elif lista_orden[i].nombre[1]>lista_orden[j].nombre[1]:
                    pass
            else:
                pass
    
    return lista_orden 
    
    

def salir():
    '''
    Funcion que pide al usuario confirmacion para salir. Retorrna un boolean.
    '''
    y_n = input("\nSeguro desea salir? [Si/No]: ")
    
    if y_n[0].upper() == "S":
        return True
    else:
        return False

def main():
    data=[]
    while True:
        opc = show_menu()
        if opc==4:
            siono=True
            while siono==True:
                data = read_file(data)
                edit_nombre= input('Ingrese el contacto que desea editar: ')
            
                print('Campos: Nombre / Apellido / Telefono fijo / Telefono movil / Email personal / Email trabajo / Fecha nac')
                edit_campo= input('¿Que campo desea editar? : ')
            
                
                x= find_contact(data,edit_nombre.lower())
                y= edit_contact(x,edit_campo.lower())
                borrada = delete_contact(data, x)
                nueva_lista = data.append(y)
                write_file('contactos.json',data)
                print('Su contacto se ha editado correctamente')
                confirma = input('Quiere seguir editando? [Si/No]:')
                if confirma[0].upper() == "S":
                    siono=True
                else:
                    siono=False 
                        
            #print("\nSelecciono la opcion", opc)
            time.sleep(3)
        elif opc == 0:
            if salir():
                
                break
        elif opc == 1:
            #esto es una prueba
                data = read_file(data)
                new_nombre= input('Ingrese el nombre: ')
                new_apellido= input('Ingrese el apellido: ')
                new_telefono_fijo = input('Ingrese telefono fijo: ')
                new_telefono_movil= input('Ingrese telefono movil: ')
                new_email_per= input('Ingrese email personal: ')
                new_email_lab= input('Ingrese email de trabajo: ')
                new_fecha_nac= input('Ingrese su fecha de nacimiento: ')
                data.append(Contacto(nombre=new_nombre,apellido=new_apellido,
                                     t_fijo=new_telefono_fijo, t_movil=new_telefono_movil,
                                     email_per=new_email_per, email_lab=new_email_lab,
                                     fecha_nac=new_fecha_nac))
                write_file('contactos.json',data)
                print('Su contacto se agrego correctamente')
        elif opc == 2:
                data = read_file(data)  #clase
                aux=list_contact(data) #clase
                for i in range(0,len(aux)):
                    print("{}. {} {}".format(i+1,aux[i].nombre,aux[i].apellido))
                #    print(aux[i])
                time.sleep(3)
        elif opc == 3:
            data = read_file(data)  #clase
            nombre = input("Ingrese el nombre o apellido: ")
            val = find_contact(data, nombre) #clase,nombre
            show_contact(val)
            time.sleep(3)
            
        elif opc == 5: #ELIMINAR
            nombre = input("Ingrese el nombre del contacto a borrar: ")
            data = read_file(data) #clase
            val = find_contact(data, nombre) #clase,nombre ingresado
            delete_contact(data, val)#clase,contacto
            print("El contacto ha sido borrado")
            time.sleep(3)
            

if __name__ == '__main__':    #Sirve para poder importar la clase sin tener que ejecutar el archivo.
    main()
#%%
#data = []
#data = read_file()
#print(data)