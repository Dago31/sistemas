from threading import Condition , Lock , Thread
import datetime
import random
import time

class TableRoom():

    def __init__(self,cant1,cant2,cant3):
        self.TableBusy = False
        self.ingredientes = {"tabaco":cant1, "papel":cant2, "cerillos":cant3}
        self.TableLock = Lock() # Agregar condiciones de ingredientes
        self.TableAvailable = Condition(self.TableLock)

    def CanIsmoke(self,tipo):
        check = True # check indica si puede fumar o no
        for elem1,elem2 in self.ingredientes.items(): # recorre la mesa viendo los ingredientes
            if elem1 != tipo and elem2 == 0: # revisa si hay cantidad necesaria de ingredientes para sacar
                check=False
        return check

    def WaitForSignal(self,tipo):
        with self.TableLock:   # Si esta requerido el monitor
            while self.TableBusy: # Verifica si necesita esperar
                self.TableAvailable.wait() # Espera hasta que alguien notifique que se dejo de usar
            
            if  self.CanIsmoke(tipo):
                time.sleep(random.randint(1,3))
                self.TableBusy = True  # Marca como ocupado la seccion mesa

    def DoneWithSmoke(self,tipo):

        if self.CanIsmoke(tipo):
            print("Fuma el tipo :", tipo)
            with self.TableLock:
                self.TableBusy = False
                for elem1,elem2 in self.ingredientes.items():#recorre los ingredientes de la mesa
                    if elem1 != tipo and elem2>0 :#resta cantidad de ingredientes que saco a la mesa
                        self.ingredientes[elem1]-=1
                self.TableAvailable.notify()
        else:
            print("No fuma  el tipo :", tipo)

class Smoker():
    def __init__(self,tipo):
        self.tipo = tipo

    def Smoke(self):
        #while True:
        print("Fumador con nombre :", self.tipo ,"requiere fumar")
        pr.WaitForSignal(self.tipo)
        # Ocupa la impresora
        pr.DoneWithSmoke(self.tipo)
        # Termina de ocupar la impresora

def Smokee(pos):
	ListOfSmokers[pos].Smoke()


pr = TableRoom(0,0,0)
ListOfSmokers = []
ListOfSmokers.append(Smoker("tabaco"))
ListOfSmokers.append(Smoker("papel"))
ListOfSmokers.append(Smoker("cerillos"))
ingredientes = ["tabaco","papel","cerillos"]
number_repeats = int(input("Ingrese cantidad de repeticiones\n"))
cnt = 0
while cnt < number_repeats:
    if pr.TableBusy == False:
        cnt+=1
        pr.ingredientes[random.choice(ingredientes)]+= 1 # Ingresa 2 ingredientes al azar
        pr.ingredientes[random.choice(ingredientes)]+= 1
        if not (pr.CanIsmoke("tabaco") or pr.CanIsmoke("papel") or pr.CanIsmoke("cerillos")):
        	print("NADIE PUEDE FUMAR")
        	print(pr.ingredientes)
        while pr.CanIsmoke("tabaco") or pr.CanIsmoke("papel") or pr.CanIsmoke("cerillos"):
            print("Actual :" , pr.ingredientes)
            arr = random.sample(xrange(1,2),3)
            for i in arr:
            	Smokee(i)
            time.sleep(random.randint(3,6))
            #pos = random.randint(0,2)
            #ListOfSmokers[pos].Smoke()
