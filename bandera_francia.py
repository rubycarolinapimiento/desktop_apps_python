#---------------------------------
# Desktop app No. 1
#---------------------------------

# se importa la libreria tkinter con todas sus funciones 
from tkinter import *

#----------------------------
# funciones de la app
#----------------------------

#-----------------------------
# ventana principal de la app
#-----------------------------

# se declara una variable llamada ventana_principal, que adquiere las caracteristicas de un objeto Tk()
ventana_principal = Tk()

# titulo de la ventana
ventana_principal.title("bandera de Francia")

# tamaño de la ventana
ventana_principal.geometry("900x450")

# deshabilitar boton de maximizar
ventana_principal.resizable(False, False)

# color de fondo de la ventana
ventana_principal.config(bg="black")

#--------------------------------
# frame azul
#--------------------------------
frame_azul = Frame(ventana_principal)
frame_azul.config(bg="blue", width=300, height=450)
frame_azul.place(x=0, y=0)

#--------------------------------
# frame blanco
#--------------------------------
frame_blanco = Frame(ventana_principal)
frame_blanco.config(bg="white", width=300, height=450)
frame_blanco.place(x=300, y=0)

#--------------------------------
# frame rojo
#--------------------------------
frame_rojo = Frame(ventana_principal)
frame_rojo.config(bg="red", width=300, height=450)
frame_rojo.place(x=600, y=0)

# run 
# se ejectua el motodo mainloop() de la clase Tk() a travez de la instancia ventana_principal. Este metodo despliega la ventana en pantalla y queda a la espera de lo que el usuario haga (click en un boton, escribir, etc). cada accion del usuario de conoce como un evento. el metodo mainloop() e un bucle infinito 
ventana_principal.mainloop()
   