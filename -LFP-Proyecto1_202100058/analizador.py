from Instrucciones.aritmeticas import *
from Instrucciones.trigonometricas import *
from Abstract.lexema import *
from Abstract.numeros import *
#from Errores.errores import *
import graphviz 
from graphviz import *

from tkinter import *
from tkinter import filedialog
from tkinter import messagebox as mb
import webbrowser as wb
from tkinter import scrolledtext as st
import tkinter as tk
import os
import sys


reserved = {
    
    'ROPERACION'        :   'Operacion',
    'RVALOR1'           :   'Valor1',
    'RVALOR2'           :   'Valor2',
    'RSUMA'             :   'Suma',
    'RRESTA'            :   'Resta',
    'RMULTIPLICACION'   :   'Multiplicacion',
    'RDIVISION'         :   'Division',
    'RPOTENCIA'         :   'Potencia',
    'RRAIZ'             :   'Raiz',
    'RINVERSO'          :   'Inverso',
    'RSENO'             :   'Seno',
    'RCOSENO'           :   'Coseno',
    'RTANGENTE'         :   'Tangente',
    'RMODULO'           :   'Modulo',
    'RTEXTO'            :   'Texto',
    'RCOLORFONDONODO'   :   'Color-Fondo-Nodo',
    'RCOLORFUENTENODO'  :   'Color-Fuente-Nodo',
    'RFORMADNODO'       :   'Forma-Nodo',
    'COMA'              :   ',',
    'PUNTO'             :   '.',
    'DPUNTOS'           :   ':',
    'CORI'              :   '[',
    'CORD'              :   ']',
    'LLAVEI'            :   '{',
    'LLAVED'            :   '}'
    
}


lexemas = list(reserved.values())

global n_linea
global n_columna
global instrucciones
global lista_lexemas

n_linea = 1
n_columna = 1
lista_lexemas = []
instrucciones = []

def instruccion(cadena):
    global n_linea
    global n_columna
    global lista_lexemas
    lexema = ''
    puntero = 0
    
    while cadena:
        
        char = cadena[puntero]
        puntero += 1
        
        if char == '\"':
            lexema, cadena = armar_lexema(cadena[puntero:])
            if lexema and cadena:
                n_columna += 1
                
                l = Lexema(lexema, n_linea, n_columna)
                
                lista_lexemas.append(l)
                n_columna += len(lexema) + 1
                puntero = 0
                
        elif char.isdigit():
            
            token, cadena = armar_numero(cadena)        
            if token and cadena:
                n_columna += 1
                
                n = Numero(token, n_linea, n_columna)
                
                lista_lexemas.append(n)
                n_columna += len(str(token)) + 1
                puntero = 0
                
        elif char == '[' or char == ']':
            
                c = Lexema(char, n_linea, n_columna)
            
                lista_lexemas.append(c)
                cadena = cadena[1:]
                puntero = 0
                n_columna += 1
        
        elif char == '\t':
            n_columna = 4
            cadena = cadena[4:]
            puntero = 0
            
        elif char == '\n':
            cadena = cadena[1:]
            puntero = 0
            n_linea = 1
            n_columna = 1
            
        else:
            cadena = cadena[1:]
            puntero = 0
            n_columna += 1

    #for lexema in lista_lexemas:
        #print(lexemas)
        
    return lista_lexemas
    
def armar_lexema(cadena):
    
    global n_linea
    global n_columna
    global lista_lexemas
    lexema = ''
    puntero = ''
    
    for char in cadena:
        puntero += char
        if char == '\"':
            return lexema, cadena[len(puntero):]
        else:
            lexema += char
        
    return None, None

def armar_numero(cadena):
    
    numero = ''
    puntero = ''
    is_decimal = False
    for char in cadena:
        puntero += char
        if char == '.':
            is_decimal = True
        if char == '"' or char  == ' ' or char == '\n' or char == ']' or char == '\t':
            if is_decimal:
                return float(numero), cadena[len(puntero):]
            else:
                return int(numero), cadena[len(puntero):]
        else:
            numero += char
            
    return None, None
    
def operar():
    
    global lista_lexemas
    global instrucciones
    operacion = ''
    n1 = ''
    n2 = ''
    
    while lista_lexemas:
        lexema = lista_lexemas.pop(0)
        if lexema.operar(None) == 'Operacion':
            operacion = lista_lexemas.pop(0)
        elif lexema.operar(None) == 'Valor1':
            n1 = lista_lexemas.pop(0)
            
            if n1.operar(None) == '[':
                n1 = operar()
                
        elif lexema.operar(None) == 'Valor2':
            n2 = lista_lexemas.pop(0)
            if n2.operar(None) == '[':
                n2 = operar()
            
        if operacion and n1 and n2:
            return Arimetica(n1,n2,operacion, f'Inicio:{operacion.getFila()}:{operacion.getColumna()}', f'Fin:{n2.getFila()}:{n2.getColumna()}')
        elif operacion and n1 and operacion.operar(None) == ('Seno' or 'Coseno' or 'Tangente'):
            return Trigonometricas(n1,operacion,f'Inicio:{operacion.getFila()}:{operacion.getColumna()}',f'Fin:{n1.getFila()}:{n1.getColumna()}')          
    return None

def operar_():
    global instrucciones
    while True:
        operacion = operar()
        if operacion:
            instrucciones.append(operacion)
        else:
            break
    for instruccion in instrucciones:
        print(instruccion.operar(None))
    return instrucciones

def buscador():
    filename=filedialog.askopenfilename(filetype="/", title="Select a file", filetypes=(("Text files","*.txt"),("all files", "*.*"),("json files", "*.json")))
    if filename!="":
        global contenido
        archi1=open(filename, "r")
        contenido=archi1.read()
        global entrada 
        entrada=contenido
        archi1.close()
        scrolledtext1.delete("1.0", tk.END)
        scrolledtext1.insert("1.0", contenido)
    global archivo 
    archivo=filename
global filename


def leer():
        archi1=open(filename, "r")
        contenido=archi1.read()   


def guardar_como():
    filename=filedialog.asksaveasfilename(initialdir="c:/pythonya",title="Guardar como", filetypes=(("txt files", "*txt"),("Todos los archivos", "*.*"),("json files", "*json")))
    if filename!="":
        archi1=open(filename,"w")
        archi1.write(scrolledtext1.get("1.0", tk.END))
        archi1.close()
        mb.showinfo("Información", "El archivo ha sido guardado con éxito.")
        global documento
        documento=archi1

def guardar():
    documento=open(archivo,"w")
    documento.write(scrolledtext1.get("1.0", tk.END))
    documento.close()
    mb.showinfo("Información", "Información guardada con éxito.")


def temasdeayuda():
    ventanaayuda=Toplevel()
    ventanaayuda.title("Información Personal")
    ventanaayuda.geometry("500x500")
    ventanaayuda.resizable(0,0)
    ventanaayuda.config(background="skyblue")
    labelnombre=Label(ventanaayuda, text="Justy Sebastian Rodríguez del Cid",font=("Arial",20), bg="black", fg="white")
    labelnombre.pack()
    labelnombre.place(x=40,y=30)

    labelcarnet=Label(ventanaayuda, text="202100058",font=("Arial",20), bg="black", fg="white")
    labelcarnet.pack()
    labelcarnet.place(x=175,y=75)

def manualusuario():
    wb.open_new(r"C:\Users\JUSTO\Desktop\-LFP-Proyecto1_202100058\Manual de Usuario.pdf")

def manualtecnico():
    wb.open_new(r"C:\Users\JUSTO\Desktop\-LFP-Proyecto1_202100058\Manual Técnico.pdf")

def salir():
    ventanaprincipal.destroy()

ventanaprincipal=Tk()
ventanaprincipal.title("Ventana principal")
ventanaprincipal.geometry("1300x500")
ventanaprincipal.resizable(0,0)
ventanaprincipal.config(background="purple")
scrolledtext1=st.ScrolledText(ventanaprincipal, width=80, height=20)
scrolledtext1.place(x=475, y=10, width=700, height=450)


botonexplorar=Button(ventanaprincipal, text="Abrir", command=buscador)
botonexplorar.pack()
botonexplorar.place(x=100, y=100, width=150, height=50)

botonguardar=Button(ventanaprincipal, text="Guardar", command=guardar)
botonguardar.pack()
botonguardar.place(x=100, y=150, width=150, height=50)


botonguardarcomo=Button(ventanaprincipal, text="Guardar Como", command=guardar_como)
botonguardarcomo.pack()
botonguardarcomo.place(x=100, y=200, width=150, height=50)

botonanalizar=Button(ventanaprincipal, text="Analizar", command=lambda:[instruccion(entrada), operar_()])
botonanalizar.pack()
botonanalizar.place(x=100, y=250, width=150, height=50)

botonerrores=Button(ventanaprincipal, text="Errores")
botonerrores.pack()
botonerrores.place(x=100, y=300, width=150, height=50)

botonsalir=Button(ventanaprincipal, text="Salir", command=salir)
botonsalir.pack()
botonsalir.place(x=100, y=350, width=150, height=50)

botonusuario=Button(ventanaprincipal, text="Manual de Usuario", command=manualusuario)
botonusuario.pack()
botonusuario.place(x=250, y=100, width=150, height=50)

botontecnico=Button(ventanaprincipal, text="Manual Técnico", command=manualtecnico)
botontecnico.pack()
botontecnico.place(x=250, y=150, width=150, height=50)

botonayuda=Button(ventanaprincipal, text="Temas de Ayuda", command=temasdeayuda)
botonayuda.pack()
botonayuda.place(x=250, y=200, width=150, height=50)

ventanaprincipal.mainloop()
