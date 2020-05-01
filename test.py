# python 3

from player import Player
import random as rd
rd.seed()


solar_farm = Player()

for t in range(48):
    production = -rd.random()*100
    load = solar_farm.compute_load(t, production)
    assert solar_farm.battery_stock[t] >= 0
    assert solar_farm.battery_stock[t] <= solar_farm.capacity
    data = {"internal" : 0.06 ,"external_purchase" : 0.1,"external_sale" : 0.03}
    imbalance = {"demand" : 0.5 , "supply" : 1}
    solar_farm.observe(t,production,data,imbalance)

    print(solar_farm.battery_stock[t])

print('test passed')