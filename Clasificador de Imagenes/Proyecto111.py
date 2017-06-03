
# coding: utf-8

# In[ ]:

from os import listdir
import os.path
from PIL import Image
import os
from Tkinter import *
from PIL import ImageTk, Image

class Imagen():
	def __init__(self, Name, Rout, Label, Weigth):
		self.Name = Name
		self.Rout = Rout
		self.Label = []
		self.Weigth = Weigth
	def __repr__(self):
		return (self.Name)


mypat = "C:\Users\Luis Manuel\Desktop\Proyecto"


class Labels():
	if os.path.isdir(mypat):
		for i in listdir(mypat):
			if os.path.isdir(mypat + "/" + i):
				pass
			elif os.path.isfile(mypat + "/" + i):
				if i.endswith(".jpg") or (".jpeg") or (".gif") or (".png"):
					root = Tk()   #INTERFAZ GRAFICA.
					img = ImageTk.PhotoImage(Image.open(mypat + "/" + i))
					panel = Label(root, image=img)
					panel.pack(side="bottom", fill="both", expand="yes")
					root.mainloop()

					etiquetas = {}  #DICCIONARIO.
					a = raw_input("Etiqueta:")
					if a in etiquetas:
						etiquetas[a].append(Imagen(i, mypat, a, os.stat(mypat + "/" + i)[6]))
					else:
						etiquetas[a] = [Imagen(i, mypat, a, os.stat(mypat + "/" + i)[6])]

					print etiquetas
					b=raw_input("Categoria:")  #CONVERTIR A METODO.
					if b in etiquetas:
						print 'Existe', len(etiquetas[b]),'imagenes en esta categoria:',etiquetas[a]
					else:
						print "No es posible encontrar esa categoria"

					c=raw_input("Imagen a buscar:")  #CONVERTIR A METODO.
					if c in etiquetas:
						print etiquetas[a]
					else:
						print "Verifique la etiqueta del elemento a acceder"
