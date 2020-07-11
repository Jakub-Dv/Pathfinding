from pathfinder import neighbours
from map_generator import Map

map1 = Map(20)
current = (6, 9)
neigs = []
for neig in neighbours(current, map1.map):
    neigs.append(neig)
print(neigs)


