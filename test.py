# python 3

from player import Player
import random as rd 
rd.seed()


solar_farm = Player()

for t in range(48):
    load = solar_farm.compute_load(t, rd.random()*100)
    assert solar_farm.battery_stock[t] >= 0
    assert solar_farm.battery_stock[t] <= solar_farm.capacity

print('test passed')