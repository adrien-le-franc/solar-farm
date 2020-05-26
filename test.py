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
    data = {"purchase" : 0.06 ,"sale" : 0.03}
    imbalance = {"purchase_cover" : 0.5 , "sale_cover" : 1}
    relative_grid_load=100
    solar_farm.observe(t,production,data,imbalance,relative_grid_load)

print('test passed')