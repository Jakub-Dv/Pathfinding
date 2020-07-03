from map_generator import Map

def FindPath(map, start=[0][0], end=None):
    if end is None:
        end = [len(map[-1]), len(map[-1])]

