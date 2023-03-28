import analizador
from analizador import *
import tkinter as Tk
from tkinter import *
from tkinter import scrolledtext as st
from tkinter import filedialog

ventanaprincipal=Tk()
ventanaprincipal.title("Ventana principal")
ventanaprincipal.geometry("1300x500")
ventanaprincipal.resizable(0,0)
ventanaprincipal.config(background="purple")
scrolledtext1=st.ScrolledText(ventanaprincipal, width=80, height=20)
scrolledtext1.place(x=475, y=10, width=700, height=450)


botonexplorar=Button(ventanaprincipal, text="Abrir", command=analizador.buscador)
botonexplorar.pack()
botonexplorar.place(x=100, y=100, width=150, height=50)

botonguardar=Button(ventanaprincipal, text="Guardar", command=analizador.guardar)
botonguardar.pack()
botonguardar.place(x=100, y=150, width=150, height=50)


botonguardarcomo=Button(ventanaprincipal, text="Guardar Como", command=analizador.guardar_como)
botonguardarcomo.pack()
botonguardarcomo.place(x=100, y=200, width=150, height=50)

botonanalizar=Button(ventanaprincipal, text="Analizar", command=lambda:[analizador.instruccion(entrada), analizador.operar_()])
botonanalizar.pack()
botonanalizar.place(x=100, y=250, width=150, height=50)

botonerrores=Button(ventanaprincipal, text="Errores")
botonerrores.pack()
botonerrores.place(x=100, y=300, width=150, height=50)

botonsalir=Button(ventanaprincipal, text="Salir", command=analizador.salir)
botonsalir.pack()
botonsalir.place(x=100, y=350, width=150, height=50)

botonusuario=Button(ventanaprincipal, text="Manual de Usuario", command=analizador.manualusuario)
botonusuario.pack()
botonusuario.place(x=250, y=100, width=150, height=50)

botontecnico=Button(ventanaprincipal, text="Manual Técnico", command=analizador.manualtecnico)
botontecnico.pack()
botontecnico.place(x=250, y=150, width=150, height=50)

botonayuda=Button(ventanaprincipal, text="Temas de Ayuda", command=analizador.temasdeayuda)
botonayuda.pack()
botonayuda.place(x=250, y=200, width=150, height=50)

ventanaprincipal.mainloop()
