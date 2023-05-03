#-----------------------------
#--------desktop NO.1---------
#-----------------------------

# se importa toda la libreria tkinter con todas sus funciones

from tkinter import *

#------------------
# funcion de la app
#------------------

#-----------------------------
# pantalla principal de la app 
#-----------------------------

# se declara una variable llamada ventana_principal que adquiera las caracteristicas de un objeto Tk()

ventana_principal= Tk()

# titulo de la ventana 

ventana_principal.title("especialidad de sistemas")

# tamaño de la ventana

ventana_principal.geometry("500x500")

# deshabilitar boton de maximizar 

ventana_principal.resizable(False,False)

# color del fondo de la ventana

ventana_principal.config(bg=("dark orange"))

#--------------------------------
# frame amarillo
#--------------------------------
frame_amarillo = Frame(ventana_principal)
frame_amarillo.config(bg="yellow", width=500, height=250)
frame_amarillo.place(x=0, y=0)

#--------------------------------
# frame azul
#--------------------------------
frame_azul = Frame(ventana_principal)
frame_azul.config(bg="blue", width=500, height=125)
frame_azul.place(x=0, y=250)

#--------------------------------
# frame rojo
#--------------------------------
frame_rojo = Frame(ventana_principal)
frame_rojo.config(bg="red", width=500, height=125)
frame_rojo.place(x=0, y=375)

# run
# se ejecuta el metodo mainloop de la clase Tk atravez de la instancia ventana_principal, este metodo despliega la ventana en pantalla

ventana_principal.mainloop()
   