from tkinter import *
from tkinter import messagebox

# funciones app
#sumar
def calcular():
    messagebox.showinfo("mini calculadora 1.0","las operaciones han sido realizadas")
    s = int(x.get()) + int(y.get())
    r = int(x.get()) - int(y.get())
    m = int(x.get()) * int(y.get())
    d = int(x.get()) / int(y.get())
    de = int(x.get()) // int(y.get())
    mod = int(x.get()) % int(y.get())
    p = int(x.get()) ** int(y.get())

    t_resultados.insert(INSERT, f"{int(x.get())} + {int(y.get())} = {s}")
    t_resultados.insert(INSERT, f"\n{int(x.get())} - {int(y.get())} = {r}")
    t_resultados.insert(INSERT, f"\n{int(x.get())} * {int(y.get())} = {m}")
    t_resultados.insert(INSERT, f"\n{int(x.get())} / {int(y.get())} = {d}")
    t_resultados.insert(INSERT, f"\n{int(x.get())} // {int(y.get())} = {de}")
    t_resultados.insert(INSERT, f"\n{int(x.get())} % {int(y.get())} = {d}") 
    t_resultados.insert(INSERT, f"\n{int(x.get())} ** {int(y.get())} = {p}")

#borar
def borrar():
    messagebox.showinfo("mini calculadora 1.0","los datos seran borrados")
    x.set("")
    y.set("")
    t_resultados.delete("1.0","end")

#salir
def salir():
    messagebox.showinfo("mini calculadora 1.0","la app se va a cerrar")
    ventana_principal.destroy()


ventana_principal= Tk()

ventana_principal.title("mini calculadora 1.0")

ventana_principal.geometry("500x500")

ventana_principal.resizable(False,False)

# color de la ventana
ventana_principal.config(bg=("blue"))

# variables globales
x=StringVar()
y=StringVar()


# frame de entrada de datos
frame_entrada = Frame(ventana_principal)
frame_entrada.config(bg="white", width=480, height=180)
frame_entrada.place(x=10, y=10)

# logo de la app
logo=PhotoImage(file="img/escudo_colegio.png")
lb_logo=Label(frame_entrada, image=logo, bg="white")
lb_logo.place(x=70,y=40)

# titulo de la app
titulo=Label(frame_entrada, text="mini calculadora 1.0")
titulo.config(bg="white", fg="blue", font=("Helvetica",20))
titulo.place(x=240,y=10)

# etiqueta para valor de x
lb_x=Label(frame_entrada, text="X =")
lb_x.config(bg="white", fg="blue",font=("Helvetica",18))
lb_x.place(x=240 , y=60)

# caja de texto para valor de x
entry_x=Entry(frame_entrada, textvariable=x)
entry_x.config(bg="white", fg="blue",font=("Time New Roman",18), width=6)
entry_x.focus_set()
entry_x.place(x=290 , y=60)

# etiqueta para valor de y
lb_y=Label(frame_entrada, text="Y =")
lb_y.config(bg="white", fg="blue",font=("Helvetica",18))
lb_y.place(x=240 , y=120)

# caja de texto para valor de y
entry_y=Entry(frame_entrada,textvariable=y)
entry_y.config(bg="white", fg="blue",font=("Time New Roman",18), width=6)
entry_y.place(x=290 , y=120)

# frame de operacion
frame_operaciones = Frame(ventana_principal)
frame_operaciones.config(bg="white", width=480, height=100)
frame_operaciones.place(x=10, y=200)

# frame del resultado
frame_resultado = Frame(ventana_principal)
frame_resultado.config(bg="white", width=480, height=180)
frame_resultado.place(x=10, y=310)

# area de texto para los resultados
t_resultados=Text(frame_resultado)
t_resultados.config(bg="black", fg="green yellow",font=("Time New Roman",20))
t_resultados.place(x=10 , y=10 ,width=460,height=160 )

# boton para sumar
bt_sumar=Button(frame_operaciones, text="CALCULAR", command=calcular)
bt_sumar.place(x=45,y=35 , width=100, height=30)

# boton para borrar
bt_borrar=Button(frame_operaciones , text="BORRAR" , command=borrar)
bt_borrar.place(x=190,y=35 , width=100, height=30)

# boton para salir
bt_salir=Button(frame_operaciones , text="SALIR", command=salir)
bt_salir.place(x=335,y=35 , width=100, height=30)

ventana_principal.mainloop()


