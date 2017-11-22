from threading import Condition , Lock , Thread
import datetime
import random
import time

class TableRoom():

    def __init__(self):
        self.TableBusy = False
        self.ingredientes = {"tabaco":0, "papel":0, "cerillos":0}
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
            print("TableBusy :", self.TableBusy , "CanIsmoke : ", self.CanIsmoke(tipo))
            while self.TableBusy: # Verifica si necesita esperar
                self.TableAvailable.wait() # Espera hasta que alguien notifique que se dejo de usar
            time.sleep(random.randint(1,6))
            if  self.CanIsmoke(tipo):
                self.TableBusy = True  # Marca como ocupado la seccion de impresiones

    def DoneWithSmoke(self,tipo):

        if self.CanIsmoke(tipo):
            print("Fuma el tipo :", tipo)
            with self.TableLock:
                self.TableBusy = False
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
        #print("Fumador con nombre :", self.tipo ,"termina de fumar")
        pr.DoneWithSmoke(self.tipo)
        # Termina de ocupar la impresora

pr = TableRoom()
ListOfSmokers = []
ListOfSmokers.append(Smoker("tabaco"))
ListOfSmokers.append(Smoker("papel"))
ListOfSmokers.append(Smoker("cerillos"))
number_repeats = int(input("Ingrese cantidad de repeticiones\n"))
for i in range(0,number_repeats):
    pos = random.randint(0,2)
    ListOfSmokers[pos].Smoke()
