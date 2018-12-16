import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
import sys

class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.labelframe1=ttk.LabelFrame(self.ventana1, text="Registrarse")
        self.labelframe1.grid(column=0, row=0, padx=10, pady=10)        
        self.agregar_componentes()
        self.agregar_menu()
        self.ventana1.mainloop()


    def agregar_componentes(self):
        self.label1=ttk.Label(self.labelframe1, text="Nombre y apellido:")
        self.label1.grid(column=0, row=0, padx=5, pady=5, sticky="e")
        self.dato1=tk.StringVar()
        self.entry1=ttk.Entry(self.labelframe1, textvariable=self.dato1)
        self.entry1.grid(column=1, row=0, padx=5, pady=5)
        self.label2=ttk.Label(self.labelframe1, text="Cédula de identidad:")
        self.label2.grid(column=0, row=1, padx=5, pady=5, sticky="e")
        self.dato2=tk.StringVar()
        self.entry2=ttk.Entry(self.labelframe1, textvariable=self.dato2)
        self.entry2.grid(column=1, row=1, padx=5, pady=5)
        self.boton1=ttk.Button (self.labelframe1, text="Aceptar", command=self.aceptar)
        self.boton1.grid(column=1, row=2, padx=5, pady=5, sticky="we")
        self.boton2=ttk.Button(self.ventana1, text="Salir", command=self.salir)
        self.boton2.grid(column=1, row=2, padx=5, pady=5, sticky="we")
         

    def agregar_menu(self):
        self.menubar1 = tk.Menu(self.ventana1)
        self.ventana1.config(menu=self.menubar1)
        self.opciones1 = tk.Menu(self.menubar1, tearoff=0)
        self.opciones1.add_command(label="Información", command=self.acerca)
        self.menubar1.add_cascade(label="Ingreso a nuevos usuarios", menu=self.opciones1)   

    def aceptar(self):
        
        if self.dato1.get()=="" or self.dato2.get()=="":
            mb.showerror("Aviso","Debe introducir un dato")
        else:
            mb.showinfo("Aviso","Usted ha sido registrado exitosamente")

    def acerca(self):
        mb.showinfo("Información", "Los usuarios deben ser mayores de edad.")

    def salir(self):
        respuesta=mb.askyesno("Cuidado", "¿Quiere salir del programa?")
        if respuesta==True:
            sys.exit()
        
        
aplicacion1=Aplicacion()
