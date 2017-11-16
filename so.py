import threading
import datetime

class Mesa(object):
	"""docstring for mesa"""
	def __init__(self, ingredientes):
		#super mesa, self.__init__()
		self.ingredientes = {"cerillos":0,"papel":0,"tabaco":0}
		self.ocupado = False

	def agregar_papel(self):
		if ocupado:
			return -1
		else
			ingredientes["papel"]+=1

	def agregar_cerillos(self):
		if ocupado:
			return -1
		else
			ingredientes["cerillos"]+=1

	def agregar_tabaco(self):
		if ocupado:
			return -1
		else
			ingredientes["tabaco"]+=1


	def sacar_cerillos(self):
		if self.cosas["cerillos"]>0:
			self.self.cosas["cerillos"]-=1
		else:
			print("no podi sacar cerillos, aweonao")
			return -1

	def sacar_papel(self):
		if self.cosas["papel"]>0:
			self.self.cosas["papel"]-=1
		else:
			print("no podi sacar papel, aweonao")
			return -1

	def sacar_tabaco(self):
		if self.cosas["tabaco"]>0:
			self.self.cosas["tabaco"]-=1
		else:
			print("no podi sacar tabaco, aweonao")
			return -1



class Fumar(Thread):
	"""docstring for Fumador"""

	def __init__(self,tipo,numId): #Inicialización
		Thread.__init__(self,tipo,numId)
		self.cv = Condition()
		self.numId = numId
		self.tipo = tipo

	def fumar(self,mesa):#Zona critica
		print("Fumador ",self.numId , " de tipo :" , self.tipo , "está fumando")
		self.cv.release() #Thread Terminó

	def poder_fumar(self):
		check = True
		for elem in mesa.ingredientes:
			if elem[1] != self.tipo and elem[1] == 0:
				check=False
		return check

	def run(self):
		check=False
		while(!check and mesa.ocupado):
			check=self.poder_fumar()
		self.cv.acquire() # Puede fumar
		mesa.ocupado = True
		for elem in mesa.ingredientes:
			if elem[1] != self.tipo and elem[1]>0:
				if elem[1] == "cerillos":
					mesa.sacar_cerillos()
				if elem[1] == "tabaco":
					mesa.sacar_tabaco()
				if elem[1] == "papel":
					mesa.sacar_papel()
		time.sleep(random.randrange(1,6,1))

class Fumador(object):
	def __init__(self,tipo,numId2):
		self.tipo=tipo
		self.numId2 = numId2
		self.creado = False

	def Crear(self):
		while !self.creado :
			pass
		new = Fumar(self.tipo,tipes)
		tipes+=1
		new.start()

	def Creado(self):
		return self.creado

print("Ingrese cuantas veces la mesa presentará objetos")
n = int(input())
mesa = Mesa()
cnt = 0
tipes = 1
ingredientes = ["cerillos","tabaco","papel"]
thread1 = Fumador("cerillos",1)
thread2 = Fumador("tabaco",2)
thread3 = Fumador("papel",3)
while True :
	if !mesa.ocupado:
		cnt+=1
		mesa.ingredientes[random.choice(ingredientes)]
		mesa.ingredientes[random.choice(ingredientes)]

		if thread1.Creado() == False:
			thread1.Crear()

		if thread2.Creado() == False:
			thread2.Crear()

		if thread3.Creado() == False:
			thread3.Crear()
