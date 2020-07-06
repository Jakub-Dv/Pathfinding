from pathfinder import neighbours
from map_generator import Map
from window import Visualization

map1 = Map(20)
current = (6, 9)
neigs = []
for neig in neighbours(current, map1.map):
    neigs.append(neig)
print(neigs)
Visualization(map1.map, path=neigs, smallest=current)
Visualization(map1.map, smallest=current)


