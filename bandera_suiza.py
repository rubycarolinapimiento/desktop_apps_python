from tkinter import*

ventana_principal=Tk()

ventana_principal.title("bandera de suiza")

ventana_principal.geometry("500x500")

ventana_principal.resizable(False, False)

ventana_principal.config(bg=("red"))

frame_blanco = Frame(ventana_principal)
frame_blanco.config(bg="cornsilk2", width=100, height=300)
frame_blanco.place(x=200, y=100)

frame_blanco = Frame(ventana_principal)
frame_blanco.config(bg="cornsilk2", width=300, height=100)
frame_blanco.place(x=100, y=200)

ventana_principal.mainloop()
 