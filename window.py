import tkinter as tk
from map_generator import Map

def Visualization(map):
    root = tk.Tk()
    root.title('Map')
    size = len(map[0]) * 10
    root.geometry(f'{size}x{size}')
    canvas = tk.Canvas(root, width=size, height=size)


    size_of_block = size / len(map[0])
    i = 0
    for block in map:
        j = 0
        for num in block:
            if num == 1:
                canvas.create_rectangle(j * size_of_block, i * size_of_block, (j + 1) * size_of_block, (i + 1) * size_of_block, fill='red')
            elif num == 'start':
                canvas.create_rectangle(j * size_of_block, i * size_of_block, (j + 1) * size_of_block, (i + 1) * size_of_block, fill='green')
            elif num == 'end':
                canvas.create_rectangle(j * size_of_block, i * size_of_block, (j + 1) * size_of_block, (i + 1) * size_of_block, fill='yellow')
            j += 1
        i += 1

    canvas.pack()
    root.mainloop()

if __name__ == '__main__':
    map1 = Map(100)
    Visualization(map1.map)