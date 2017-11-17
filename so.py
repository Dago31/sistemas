from threading import Condition , Lock , Thread
import datetime
import random
import time
class Mesa(object):
	"""docstring for mesa"""
	def __init__(self):
		#super mesa, self.__init__()
		self.ingredientes = {"cerillos":0,"papel":0,"tabaco":0}
		self.ocupado = False

	def agregar_papel(self):
		if ocupado:
			return -1
		else:
			ingredientes["papel"]+=1

	def agregar_cerillos(self):
		if ocupado:
			return -1
		else:
			ingredientes["cerillos"]+=1

	def agregar_tabaco(self):
		if ocupado:
			return -1
		else:
			ingredientes["tabaco"]+=1


	def sacar_cerillos(self):
		if self.ingredientes["cerillos"]>0:
			self.ingredientes["cerillos"]-=1
		else:
			print("no podi sacar cerillos, aweonao")
			return -1

	def sacar_papel(self):
		if self.ingredientes["papel"]>0:
			self.ingredientes["papel"]-=1
		else:
			print("no podi sacar papel, aweonao")
			return -1

	def sacar_tabaco(self):
		if self.ingredientes["tabaco"]>0:
			self.ingredientes["tabaco"]-=1
		else:
			print("no podi sacar tabaco, aweonao")
			return -1



class Fumar(Thread):
	"""docstring for Fumador"""

	def __init__(self,tipo,numId): #Inicializacion
		Thread.__init__(self)
		self.cv = Condition()
		self.numId = numId
		self.tipo = tipo

	def fumar(self):#Zona critica
		print("Fumador ",self.numId , " de tipo :" , self.tipo , "termina de fumar")
		self.cv.release() #Thread Termino
		mesa.ocupado=False

	def run(self):
		#print("corriendo Thread :",self.numId,"con tipo :",self.tipo)
		check=False
		while not check:
			check=poder_fumar(self.tipo,mesa)
		self.cv.acquire() # Puede fumar
		mesa.ocupado = True
		for elem1,elem2 in mesa.ingredientes.items():
			if elem1 != self.tipo and elem2>0:
				if elem1 == "cerillos":
					mesa.sacar_cerillos()
				if elem1 == "tabaco":
					mesa.sacar_tabaco()
				if elem1 == "papel":
					mesa.sacar_papel()
		time.sleep(random.randrange(1,6,1))
		Fumar.fumar(self)

def poder_fumar(tipo,mesa):
	check = True
	if mesa.ocupado == True:
		return False
	for elem1,elem2 in mesa.ingredientes.items():
		if elem1 != tipo and elem2 == 0:
			check=False
	return check


class Fumador(object):
	def __init__(self,tipo,numId2):
		self.tipo=tipo
		self.numId2 = numId2
		self.creado = False

	def Crear(self,tipes):
		while self.creado == True:
			pass
		self.creado = True
		nuevoThread = Fumar(self.tipo,tipes)
		tipes+=1
		nuevoThread.start()
		print("Creando thread desde Fumador Nro : ",self.numId2,"Thread id :",tipes , " Con tipo :" , self.tipo)


	def Creado(self):
		return self.creado

print("Ingrese cuantas veces la mesa presentara objetos")
n = int(input())
mesa = Mesa()
cnt = 0
tipes = 1
ingredientes = ["cerillos","tabaco","papel"]
thread1 = Fumador("cerillos",1)
thread2 = Fumador("tabaco",2)
thread3 = Fumador("papel",3)
while cnt < n :

	if not mesa.ocupado:
		cnt+=1
		mesa.ingredientes[random.choice(ingredientes)]+=1
		mesa.ingredientes[random.choice(ingredientes)]+=1
		print("Ingredientes agregados en la mesa",mesa.ingredientes)
		if thread1.Creado() == False and poder_fumar(thread1.tipo,mesa):
			thread1.Crear(tipes)
			tipes+=1

		if thread2.Creado() == False and poder_fumar(thread2.tipo,mesa):
			thread2.Crear(tipes)
			tipes+=1

		if thread3.Creado() == False and poder_fumar(thread3.tipo,mesa):
			thread3.Crear(tipes)
			tipes+=1