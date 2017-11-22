from threading import Condition , Lock , Thread
import datetime
import random
import time

terminado=""


class Mesa(object):#objeto mesa que va guardar los ingredientes
	"""docstring for mesa"""
	def __init__(self):
		#super mesa, self.__init__()
		self.ingredientes = {"cerillos":0,"papel":0,"tabaco":0}#variable para guardar cantidad de ingredientes
		self.ocupado = False#verifica el estado de la mes

	def agregar_papel(self):#agrega papel si no esta ocupada la mesa
		if ocupado:
			return -1
		else:
			ingredientes["papel"]+=1

	def agregar_cerillos(self):#agrega cerillos si no esta ocupada la mesa
		if ocupado:
			return -1
		else:
			ingredientes["cerillos"]+=1

	def agregar_tabaco(self):#agrega tabaco si no esta ocupada la mesa
		if ocupado:
			return -1
		else:
			ingredientes["tabaco"]+=1


	def sacar_cerillos(self):#saca cerillos si hay cantidad de estos
		if self.ingredientes["cerillos"]>0:
			self.ingredientes["cerillos"]-=1
		else:
			print("no podi sacar cerillos, aweonao")
			return -1

	def sacar_papel(self):#saca papel si hay cantida de estos
		if self.ingredientes["papel"]>0:
			self.ingredientes["papel"]-=1
		else:
			print("no podi sacar papel, aweonao")
			return -1

	def sacar_tabaco(self):#saca tabaco si hay cantidad de estos
		if self.ingredientes["tabaco"]>0:
			self.ingredientes["tabaco"]-=1
		else:
			print("no podi sacar tabaco, aweonao")
			return -1

mesa = Mesa()#crea la mesa

class Fumar(Thread): #Thread para controlar cuando fumar
	"""docstring for Fumador"""

	def __init__(self,tipo,numId): #Inicializacion
		Thread.__init__(self)
		self.cv = Condition()
		self.numId = numId#id del fumador
		self.tipo = tipo#tipo de fumador

	def fumar(self):#Zona critica
		self.cv.release() #Thread Termino
		mesa.ocupado=False
		terminado=self.tipo
		print("El thread nro:",self.numId , " de tipo :" , self.tipo , "ha terminado de fumar")



	def run(self):#revisa en cada instante si puede fumar
		#print("corriendo Thread :",self.numId,"con tipo :",self.tipo)
		check=False
		while not check and not mesa.ocupado :#revia si puede fumar
			check=poder_fumar(self.tipo,mesa)
		
		print("tipo "+self.tipo)
		mesa.ocupado = True#la mesa pasa a estar  ocupada por que hay alguien fumando
		self.cv.acquire() # Puede fumar
		print( "Inicia thread :",self.tipo)
		for elem1,elem2 in mesa.ingredientes.items():#recorre los ingredientes de la mesa
			if elem1 != self.tipo and elem2>0 :#resta cantidad de ingredientes que saco a la mesa
				if elem1 == "cerillos":
					mesa.sacar_cerillos()
				if elem1 == "tabaco":
					mesa.sacar_tabaco()
				if elem1 == "papel":
					mesa.sacar_papel()
		
		time.sleep(random.randrange(1,3,1))#tiempo random en que demora fumar
		Fumar.fumar(self)#comienza a fumar

def poder_fumar(tipo,mesa):#verifica si puede fumar
		check = True#check indica si puede fumar o no
		if mesa.ocupado == True:#verifica si la mesa esta desocupada
			return False
		for elem1,elem2 in mesa.ingredientes.items():#recorre la mesa viendo los ingredientes
			if elem1 != tipo and elem2 == 0:#revisa si hay cantidad necesaria de ingredientes para sacar
				check=False
		return check


def send(terminado,num_thread):
	aux = Fumar(terminado,num_thread)
	aux.start()

print("Ingrese cuantas veces la mesa presentara objetos")
n = int(input())#cuantos ingredientes se anadiran a la mesa
#n=2
cnt = 0#contador para revisar iteraciones
num_thread = 1
ingredientes = ["cerillos","tabaco","papel"]#crea los ingredientes

cola = ["cerillos","papel","tabaco"]
while cnt < n :
	if not mesa.ocupado:#mientras la mesa no este ocupada
		print("Disponible para retirar ingredientes")
		cnt += 1
		mesa.ingredientes[random.choice(ingredientes)]+=1#ingresa 2 ingredientes al azar
		mesa.ingredientes[random.choice(ingredientes)]+=1
		print("Ingredientes agregados en la mesa",mesa.ingredientes)
		while poder_fumar("cerillos",mesa) or poder_fumar("tabaco",mesa) or poder_fumar("papel",mesa)  :
			aux = cola.pop(0)
			if poder_fumar(aux,mesa):
				send(aux,num_thread)
				num_thread+=1

			#print("inserto"+aux)
			cola.append(aux)
			time.sleep(random.randrange(3,6,1))

		#print ("sale del segundo ")
print("termina de poner ingrediente")
