#-------------------------
# Desktop apps No. 1
#-------------------------

# se importa la libreria tkinter con todas sus funciones 
from tkinter import *

#-------------------------
# funciones de la app
#-------------------------

#-------------------------
# ventana  principal de la app
#--------------------------

# se declara una variable llamada ventana_principal, que adquiere las caracteristicas de un objetivo Tk()
ventana_principal = Tk()

# titulo de  ventana
ventana_principal.title("Bandera de francia")

#tamaño de la ventana 
ventana_principal.geometry("900x500")

# deshabiltar boton de maximizar 
ventana_principal.resizable(False, False)

# color de fondo de la ventana 
ventana_principal.config(bg="black")

#------------------------------
# frame azul 
#-----------------------------
frame_azul = Frame(ventana_principal)
frame_azul.config(bg="navy", width=300, height=500)
frame_azul.place(x=0, y=0)

#------------------------------
# frame blanco
#-----------------------------
frame_blanco= Frame(ventana_principal)
frame_blanco.config(bg="white", width=300, height=500)
frame_blanco.place(x=300, y=0)

#------------------------------
# frame rojo
#-----------------------------
frame_rojo= Frame(ventana_principal)
frame_rojo.config(bg="red3", width=300, height=500)
frame_rojo.place(x=600, y=0)

# run
# # se el metodo mainloop()de la clase Tk(a través de la instancia ventana_principal.Este metodo despliega la ventana en pantalla y queda a la espera de lo que el usuario haga (click en un boton, escribir, etc). Cada acción del usuario se conoce un evento. El método mainloop() es un bucle infinito.

ventana_principal.mainloop()
