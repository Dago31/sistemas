import datetime
class Mesa(object):
	"""docstring for Monitor"""
	def __init__(self, arg):
		#super(Monitor, self).__init__()
		self.ingredientes = {"cerillos" : 0 , "papel" : 0 , "tabaco" : 0}

	def cant_cerillos(self):
		return self.cosas["cerillos"]

	def cant_papel(self):
		return self.cosas["papel"]

	def cant_tabaco(self):
		return self.cosas["tabaco"]

	def sacar_cerillos(self):
		if(self.cosas["cerillos"]>0):
			self.self.cosas["cerillos"]-=1
		else:
			print("no podi sacar cerillos, aweonao")
			return -1

	def sacar_papel(self):
		if(self.cosas["papel"]>0):
			self.self.cosas["papel"]-=1
		else:
			print("no podi sacar papel, aweonao")
			return -1

	def sacar_tabaco(self):
		if(self.cosas["tabaco"]>0):
			self.self.cosas["tabaco"]-=1
		else:
			print("no podi sacar tabaco, aweonao")
			return -1
	def agregar_cerillos(self,cantidad):
		self.cosas["cerillos"]+=cantidad

	def agregar_papel(self,cantidad):
		self.cosas["papel"]+=cantidad

	def agregar_tabaco(self,cantidad):
		self.cosas["tabaco"]+=cantidad



class Fumador(object):
	def __init__(self,args):
		#super(Monitor, self).__init__()
		self.ingredientes = {"cerillos" : 0 , "papel" : 0 , "tabaco" : 0}
		self.tiempo_fu = cmath.rand(1,100)
		self.time_ini = 0
		self.punish = 0

	def fumar(self):
		self.ingredientes["cerillos"]-=1
		self.ingredientes["papel"]-=1
		self.ingredientes["tabaco"]-=1
		self.time_ini = datetime.now()

	def check_punish(self):
		

def Process(Mesa,Fumadores): #L
	ingredientes = ["cerillos","tabaco","papel"]
	for i in range(1..100):
		x = random.choice(ingredientes)
		y = random.choice(ingredientes)
		if 

		