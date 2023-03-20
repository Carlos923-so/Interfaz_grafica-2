from tkinter import *
from tkinter import ttk
import tkinter as tk


raiz = Tk()
raiz.title("Ejercicio2")
raiz.geometry("700x600")
raiz.config(bg="white")

imagen1 = PhotoImage(file="imagen2.png")
imagen2 = PhotoImage(file="lupa.png")
imagen3 = PhotoImage(file="lupa.png")

respaldo=Frame(raiz,bg="black")
respaldo.grid(column=0,row=0)

grisFrame=Frame(respaldo, bg="gray40") #Widgets transparentes #Instancia de raiz
grisFrame.grid(column=0, row=0,sticky=W)


btnImagen=Label(grisFrame,borderwidth=(0))
btnImagen.grid(column=0,row=0,sticky=(W))
btnImagen['image'] = imagen1

#blackFrame=Frame(raiz, background="black",width=450,height=450 ) #Widgets transparentes #Instancia de raiz
#blackFrame.grid(column=0, row=1, padx=0)


tintoFrame=Frame(respaldo, background="#482525",width=500, height=500 ) #Widgets transparentes #Instancia de raiz
tintoFrame.grid(column=0, row=1, padx=15, pady=7)

"""auxiliarFrame=Frame(raiz, background="#482525",width=500, height=500 ) #Widgets transparentes #Instancia de raiz
auxiliarFrame.grid(column=0, row=1, padx=15, pady=7)"""

'''tinto2Frame=Frame(raiz, bg="coral4",width=500, height=400) #Widgets transparentes #Instancia de raiz
tinto2Frame.grid(column=0, row=3, pady=0)'''

tinto3Frame=Frame(respaldo, bg="coral4",width=1200, height=100) #Widgets transparentes #Instancia de raiz
tinto3Frame.grid(column=0, row=3, pady=0)
"""tinto5Frame=Frame(tintoFrame, bg="coral4",width=15, height=15) #Widgets transparentes #Instancia de raiz
tinto5Frame.grid(column=2, row=0, pady=0)"""

#tinto4Frame=Frame(tintoFrame, bg="coral4",width=500, height=400) #Widgets transparentes #Instancia de raiz
#tinto4Frame.grid(column=0, row=5, pady=0)

'''btnImagen1=ttk.Label(tintoFrame,borderwidth=(0))
btnImagen1.grid(column=2,row=0,sticky=(W))
btnImagen1['image'] = imagen2'''


btnImagen2=Label(tintoFrame,borderwidth=0)
btnImagen2.grid(column=2,row=0,sticky=(W),padx=100)
btnImagen2['image'] = imagen3


produc=Label(grisFrame, text="Product management",bg="gray40",font=("Arial black", 28),fg="white")
produc.grid(column=1,row=0,padx=10)

id=Label(tintoFrame, text="Id product",font=("Arial black",12),background="#482525",fg="white")
id.grid(column=0, row=0 ,padx=0,pady=10,sticky=(W))

Name=Label(tintoFrame, text="Name",font=("Arial black",12),background="#482525",fg="white")
Name.grid(column=0, row=1,padx=0,pady=10,sticky=(W))
Description=Label(tintoFrame, text="Description",font=("Arial black",12),background="#482525",fg="white")
Description.grid(column=0, row=2 ,padx=0,pady=10,sticky=(W))
quiantity=Label(tintoFrame, text="quiantity",font=("Arial black",12),background="#482525",fg="white")
quiantity.grid(column=0, row=3 ,padx=0,pady=10,sticky=(W))
price=Label(tintoFrame, text="Price",font=("Arial black",12),background="#482525",fg="white")
price.grid(column=0, row=4 ,padx=0,pady=30,sticky=(W))
numero=Label(tintoFrame, text="6",font=("Arial black",12),background="#482525",fg="white")
numero.grid(column=1, row=0 ,padx=20,pady=10,sticky=(W))
# Añadimos la línea horizontal al Canvas
"""auxiliar=Label(auxiliarFrame,text="5")
auxiliar.grid(column=0,row=0)"""
facto=Label(tintoFrame, text="Facto",font=("Arial black",12),background="#482525",fg="white")
facto.grid(column=1, row=1,padx=20,pady=20,sticky=(W))
cafe=Label(tintoFrame, text="Cafe",font=("Arial black",12),background="#482525",fg="white")
cafe.grid(column=1, row=2 ,padx=20,pady=20,sticky=(W))
precio=Label(tintoFrame, text="7000",font=("Arial black",12),background="#482525",fg="white")
precio.grid(column=1, row=3 ,padx=20,pady=10,sticky=(W))
segundoprecio=Label(tintoFrame, text="600.0",font=("Arial black",12),background="#482525",fg="white")
segundoprecio.grid(column=1, row=4 ,padx=20,pady=30,sticky=(W))
save=Button(tintoFrame, text="Save", bg="green", fg="white", width=10,font=("Arial black",12))
save.grid(column=2,row=1,padx=0)
delete=Button(tintoFrame, text="Delete",font=("Arial black",12), bg="red", fg="white", width=10)
delete.grid(column=2,row=2)
back=Button(tintoFrame, text="Back",font=("Arial black",12), bg="#482525", fg="medium purple",borderwidth=(0))
back.grid(column=2,row=0,sticky=(E),padx=0)
boton3=Button(tintoFrame, text="Update",font=("Arial black",12), bg="yellow", fg="white", width=10,height=0)
boton3.grid(column=2,row=3)

tabla = ttk.Treeview(tinto3Frame, height=8, columns=("col1", "col2", "col3", "col4"))
tabla.column("#0", width=105)
tabla.column("col1", width=110, anchor=CENTER)
tabla.column("col2", width=110, anchor=CENTER)
tabla.column("col3", width=110, anchor=CENTER)
tabla.column("col4", width=105, anchor=CENTER)

tabla.heading("#0", text="idproduct", anchor=CENTER)
tabla.heading("col1", text="namep", anchor=CENTER)
tabla.heading("col2", text="description", anchor=CENTER)
tabla.heading("col3", text="quantity", anchor=CENTER)
tabla.heading("col4", text="unite_price", anchor=CENTER)



tabla.insert("", END, text="1", values=("Condia", "lait", "24", "100.0"))
tabla.insert("", END, text="2", values=("la vache quirit", "fromage", "200", "300.0"))
tabla.insert("", END, text="3", values=("hamoud boualam", "boisson gaseuse", "98", "90.0"))
tabla.insert("", END, text="4", values=("Mina", "chocolat", "80", "50.0"))
tabla.insert("", END, text="5", values=("Aroma", "cafe", "60", "80.0"))
tabla.insert("", END, text="6", values=("Facto", "facto", "7000", "600.0"))

tabla.pack()

barra = Scrollbar(tabla, width=17).place(x=523, y=1)

raiz.mainloop()
