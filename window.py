import tkinter as tk
from map_generator import Map

def Visualization(map, path=None, smallest=None):
    if type(path) == ValueError:
        print('No path exists')
        return False

    root = tk.Tk()
    root.title('Map')
    size = len(map[0]) * 20
    root.geometry(f'{size}x{size}')
    canvas = tk.Canvas(root, width=size, height=size)

    size_of_block = size / len(map[0])
    if path:
        for p in path:
            canvas.create_rectangle(p[1] * size_of_block, p[0] * size_of_block, (p[1] + 1) * size_of_block, (p[0] + 1) * size_of_block, fill='blue')

    for i, block in enumerate(map):
        for j, num in enumerate(block):
            if not num:
                canvas.create_rectangle(j * size_of_block, i * size_of_block, (j + 1) * size_of_block, (i + 1) * size_of_block, fill='red')
            elif num == 'start':
                canvas.create_rectangle(j * size_of_block, i * size_of_block, (j + 1) * size_of_block, (i + 1) * size_of_block, fill='green')
            elif num == 'end':
                canvas.create_rectangle(j * size_of_block, i * size_of_block, (j + 1) * size_of_block, (i + 1) * size_of_block, fill='yellow')
    if smallest:
        canvas.create_rectangle(list(smallest)[1] * size_of_block, list(smallest)[0] * size_of_block, (list(smallest)[1] + 1) * size_of_block, (list(smallest)[0] + 1) * size_of_block, fill='violet')

    canvas.pack()
    root.mainloop()


if __name__ == '__main__':
    map1 = Map(100)
    Visualization(map1.map)