import numpy as np
import os
from numpy.random import randint

class SolarFarm:
    def __init__(self):
        self.dt = 0.5
        self.efficiency=0.95
        self.scenario = {}
        self.bill = np.zeros(48) # prix de vente de l'électricité
        self.load_battery = np.zeros(48) # chargement de la batterie (li)
        self.battery_stock = np.zeros(49) #a(t)
        self.capacity =100 #vérifier
        self.max_load=70 #vérifier


    def update_battery_stock(self, time, load):
        if abs(load) > self.max_load:
            load = self.max_load*np.sign(load) #saturation au maximum de la batterie

        new_stock = self.battery_stock[time] + (self.efficiency*max(0,load) - 1/self.efficiency * max(0,-load))*self.dt

        #On rétablit les conditions si le joueur ne les respecte pas :
        if new_stock < 0: #impossible, le min est 0, on calcule le load correspondant
            load = - self.battery_stock[time] / (self.efficiency*self.dt)
            new_stock = 0

        elif new_stock > self.capacity:
            load = (self.capacity - self.battery_stock[time]) / (self.efficiency*self.dt)
            new_stock = self.capacity

        self.battery_stock[time+1] = new_stock
        return load

    def compute_load(self,time):
        load = self.load_battery[time]
        lo = self.update_battery_stock(self, time, load)
        self.load_battery[time] = lo 
