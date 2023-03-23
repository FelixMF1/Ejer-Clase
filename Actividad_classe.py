from tkinter import *

ventana = Tk()
ventana.geometry("500x450")
ventana.title("Iniciar Sesión")

lbl_usuario = Label(ventana, text="Usuario")
lbl_usuario.pack()

entrada_usuario = Entry(ventana)
entrada_usuario.pack()

lbl_contrasena = Label(ventana, text="Contraseña")
lbl_contrasena.pack()

entrada_contrasena = Entry(ventana, show="*")
entrada_contrasena.pack()

lbl_confirmacion = Label(ventana, text="Confirmar Contraseña")
lbl_confirmacion.pack()

entrada_confirmacion = Entry(ventana, show="*")
entrada_confirmacion.pack()

def iniciar_sesion():
    if entrada_contrasena.get() == entrada_confirmacion.get():
        print("Sesión iniciada")
        ventana.configure(bg="green")
    else:
        print("Contraseña incorrecta")


boton_iniciar_sesion = Button(ventana, text="Iniciar Sesión", command=iniciar_sesion)
boton_iniciar_sesion.pack()

lbl_genero = Label(ventana, text="")
lbl_genero.pack()

var_genero = StringVar()
var_genero.set("N/A")

rbt_masculino = Radiobutton(ventana, text="Masculino", variable=var_genero, value="M")
rbt_masculino.pack()

rbt_femenino = Radiobutton(ventana, text="Femenino", variable=var_genero, value="F")
rbt_femenino.pack()

lbl_terminos = Label(ventana, text="")
lbl_terminos.pack()

var_terminos = BooleanVar()
var_terminos.set(False)

chk_terminos = Checkbutton(ventana, text="Acepto los términos y condiciones", variable=var_terminos)
chk_terminos.pack()

ventana.mainloop()
