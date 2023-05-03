from tkinter import *

ventana_principal=Tk()

ventana_principal.title("bandera de noruega")

ventana_principal.geometry("900x500")

ventana_principal.resizable(False, False)

ventana_principal.config(bg=("firebrick3"))

frame_blanca = Frame(ventana_principal)
frame_blanca.config(bg="cornsilk2", width=100, height=900)
frame_blanca.place(x=275, y=0)

frame_blanca = Frame(ventana_principal)
frame_blanca.config(bg="cornsilk2", width=900, height=100)
frame_blanca.place(x=0, y=225)

frame_azul = Frame(ventana_principal)
frame_azul.config(bg="navy", width=50, height=900)
frame_azul.place(x=300, y=0)

frame_azul = Frame(ventana_principal)
frame_azul.config(bg="navy", width=900, height=50)
frame_azul.place(x=0, y=250)

ventana_principal.mainloop()
