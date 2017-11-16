import threading
import datetime

class mesa(object):
	"""docstring for mesa"""
	def __init__(self, ingredientes):
		#super mesa, self.__init__()
		self.ingredientes = {"fosforos":´0,"papelillos":0,"mota":0}

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

class Fumador(Thread):
	"""docstring for Fumador"""
	def __init__(self, ing_propios,numId):
		#super(Fumador, self).__init__()
		self.ing_propios = ing_propios
		self.ocupado = False
		self.numId = numId

def fumar(Fumador, mesa):
	if mesa
		
