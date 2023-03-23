from tkinter import*
#from PIL import ImageTk,Image 


root= Tk()
ventanaprincipal=Frame(root,bg="#0ff")
ventanaprincipal.grid()
contras=StringVar()
confirmo=StringVar()

def contraseñas():
    if contras.get()==confirmo.get():
        print("SESION INICIADA")
        ventanaprincipal.config(bg="#0ff")
        

        
    else:
        print("CONTRASEÑA INCORRECTA")

#NOTA DESCARGAR LA LIBRERIA PARA Q FUNCIONE ESTA PARTE DEL CODIGO
#imagen
#img=Image.open("C:\Users\User\Pictures\Screenshots")
#imagenmusica=img.resize((100,100))
#imag=ImageTk.PhotoImage(imagenmusica)
#mititulo=Label(ventanaprincipal,image=imag)
#mititulo.grid(row=1,column=1,padx=10,pady=20,columnspan=2,rowspan=2)

titulo=Label(ventanaprincipal,text="LOG IN", bg="#0ff",font=("Glossy Sheen",20))
titulo.grid(row=3,column=1,columnspan=2)

name=Label(ventanaprincipal,text="NOMBRE:", bg="#0ff",font=("Roboto",15)).grid(row=4,column=1,padx=30,pady=30)
textonombre=Entry(ventanaprincipal,font=("roboto",15)).grid(row=4,column=2,padx=15,pady=15)

contra=Label(ventanaprincipal, bg="#0ff",text="CONTRASEÑA:",font=("Roboto",15)).grid(row=5,column=1,padx=15,pady=30)
textocontra=Entry(ventanaprincipal,font=("roboto",15),textvariable=contras).grid(row=5,column=2,padx=30,pady=15)

comfir_contra=Label(ventanaprincipal, bg="#0ff",text="CONFIRMAR CONTRASEÑA:",font=("Roboto",15)).grid(row=6,column=1,padx=15,pady=30)
textoconfir=Entry(ventanaprincipal,font=("roboto",15),textvariable=confirmo).grid(row=6,column=2,padx=30,pady=15)
control1=IntVar()

hpmbre=Checkbutton(ventanaprincipal, text="HOMBRE",variable=control1, bg="#0ff",font=("Roboto",15))
hpmbre.grid(row=7,column=1)
control2=IntVar()

mujer=Checkbutton(ventanaprincipal, text="MUJER",variable=control2, bg="#0ff",font=("Roboto",15))
mujer.grid(row=7,column=2)
control3=IntVar()

aceptar=Checkbutton(ventanaprincipal, text="ACEPTO TERMINOS",variable=control3, bg="#0ff",font=("Roboto",15))
aceptar.grid(row=8,column=1,columnspan=2)

iniciar=Button(ventanaprincipal,text="INICIAR",command=contraseñas,width=20,height=2).grid(row=9,column=1,columnspan=2)

root.mainloop()


