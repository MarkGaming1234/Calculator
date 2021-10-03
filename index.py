import tkinter 
from tkinter.constants import END
import math


wd=9
hg=5
i=0

ventana = tkinter.Tk()
ventana.geometry("416x400")
ventana.title("Calculator")
ventana.iconbitmap("icono.ico")
ventana.config(bg="sandy brown")


def nv1(valor):
   global i
   Input.insert(i,valor)
   i += 1
   
def borrar():
    Input.delete(0,END)   
    i=0

def hacer_operacion():
    ecuacion = Input.get()
    Resultado=eval(ecuacion)
    Input.delete(0,END)
    Input.insert(0,Resultado)
    i=0



Input=tkinter.Entry(ventana,width=20)
nu1=tkinter.Button(ventana,text="1",width=wd,height=hg,bg="DodgerBlue4",command=lambda: nv1(1))
nu2=tkinter.Button(ventana,text="2",width=wd,height=hg,command=lambda: nv1(2),bg="DodgerBlue4")
nu3=tkinter.Button(ventana,text="3",width=wd,height=hg,command=lambda: nv1(3),bg="DodgerBlue4")
nu4=tkinter.Button(ventana,text="4",width=wd,height=hg,command=lambda: nv1(4),bg="DodgerBlue4")
nu5=tkinter.Button(ventana,text="5",width=wd,height=hg,command=lambda: nv1(5),bg="DodgerBlue4")
nu6=tkinter.Button(ventana,text="6",width=wd,height=hg,command=lambda: nv1(6),bg="DodgerBlue4")
nu7=tkinter.Button(ventana,text="7",width=wd,height=hg,command=lambda: nv1(7),bg="DodgerBlue4")
nu8=tkinter.Button(ventana,text="8",width=wd,height=hg,command=lambda: nv1(8),bg="DodgerBlue4")
nu9=tkinter.Button(ventana,text="9",width=wd,height=hg,command=lambda: nv1(9),bg="DodgerBlue4")
nu0=tkinter.Button(ventana,text="0",width=wd,height=hg,command=lambda: nv1(0),bg="DodgerBlue4")


#config=tkinter.Button(ventana,text="Configurar",width=wd,height=2,bg="honeydew2",command=configurar)    

Igual=tkinter.Button(ventana,text="=",width=wd,height=hg,bg="honeydew2",command=lambda: hacer_operacion())
suma=tkinter.Button(ventana,text="+",width=wd,height=hg,command=lambda: nv1("+"),bg="ivory4")
resta=tkinter.Button(ventana,text="-",width=wd,height=hg,command=lambda: nv1("-"),bg="ivory4")
mult=tkinter.Button(ventana,text="x",width=wd,height=hg,command=lambda: nv1("*"),bg="ivory4")
div=tkinter.Button(ventana,text="÷",width=wd,height=hg,command=lambda: nv1("/"),bg="ivory4")
delete=tkinter.Button(ventana,width=wd,height=hg,command=borrar,text="AC",bg="honeydew2")
elv2=tkinter.Button(ventana,text="x²",width=wd,height=hg,command=lambda: nv1("**2"),bg="salmon4")
elvx=tkinter.Button(ventana,text="^",width=wd,height=hg,command=lambda: nv1("**"),bg="salmon4")
raizc=tkinter.Button(ventana,text="2√",width=wd,height=hg,command=lambda: nv1("**0.5"),bg="salmon4")
#raiz3=tkinter.Button(ventana,text="3√",width=wd,height=hg,command=lambda: nv1("**0.333"))
pi=tkinter.Button(ventana,text="π",width=wd,height=hg,command=lambda: nv1("3.141592"),bg="salmon4")

Input.grid(row=1,column=5)
#config.grid(row=1,column=1)
nu0.grid(row=5,column=1,padx=2,pady=2)
nu1.grid(row=2,column=1,padx=2,pady=2)
nu2.grid(row=2,column=2,padx=2,pady=2)
nu3.grid(row=2,column=3,padx=2,pady=2)
nu4.grid(row=3,column=1,padx=2,pady=2)
nu5.grid(row=3,column=2,padx=2,pady=2)
nu6.grid(row=3,column=3,padx=2,pady=2)
nu7.grid(row=4,column=1,padx=2,pady=2)
nu8.grid(row=4,column=2,padx=2,pady=2)
nu9.grid(row=4,column=3,padx=2,pady=2)
Igual.grid(row=5,column=2,padx=2,pady=2)
suma.grid(row=2,column=4,padx=2,pady=2)
resta.grid(row=3,column=4,padx=2,pady=2)
mult.grid(row=4,column=4,padx=2,pady=2)
div.grid(row=5,column=4,padx=2,pady=2)
delete.grid(row=5,column=3,padx=2,pady=2)
elv2.grid(row=2,column=5)
elvx.grid(row=3,column=5)
raizc.grid(row=4,column=5)
#raiz3.grid(row=5,column=5)
pi.grid(row=5,column=5)


ventana.mainloop()
