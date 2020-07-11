import tkinter as tk
from map_generator import Map
from pathfinder import AStar


class GUI:
    def __init__(self, root):
        self.root = root
        root.title('Map')
        self.map = []

        self.canvas = tk.Canvas(self.root, width=800, height=800)
        self.canvas.pack(side='right', fill='both')

        self.create_map_button = tk.Button(width=20, height=3, text='Generate Maze', command=self.generate_maze)
        self.create_map_button.pack(pady=10)

        self.solve_map_button = tk.Button(width=20, height=3, text='Solve Maze', command=self.solve_map)
        self.solve_map_button.pack(pady=20)

        self.clear_button = tk.Button(width=20, height=3, text='Clear board', command=self.clear_board)
        self.clear_button.pack(pady=20)

        self.quit_gui = tk.Button(width=20, height=3, text='Exit', command=self.root.quit)
        self.quit_gui.pack(side='bottom', pady=30)

    def generate_maze(self):
        self.canvas.create_rectangle(0, 0, 800, 800, fill='white')
        self.map = Map(40, random=False)
        for i, block in enumerate(self.map.map):
            for j, num in enumerate(block):
                if not num:
                    self.canvas.create_rectangle(j * 20, i * 20, (j + 1) * 20, (i + 1) * 20, fill='red')

        if self.map.start:
            self.canvas.create_rectangle(list(self.map.start)[1] * 20, list(self.map.start)[0] * 20, (list(self.map.start)[1] + 1) * 20, (list(self.map.start)[0] + 1) * 20, fill='green')
        if self.map.end:
            self.canvas.create_rectangle(list(self.map.end)[1] * 20, list(self.map.end)[0] * 20, (list(self.map.end)[1] + 1) * 20, (list(self.map.end)[0] + 1) * 20, fill='yellow')


    def solve_map(self):
        if not self.map == []:
            path = AStar(self.map.map, self.map.start, self.map.end)
            if path:
                for p in path:
                    if not p == self.map.end and not p == self.map.start:
                        self.canvas.create_rectangle(p[1] * 20, p[0] * 20, (p[1] + 1) * 20, (p[0] + 1) * 20, fill='blue')

    def clear_board(self):
        self.map = []
        self.canvas.delete('all')


if __name__ == '__main__':
    root = tk.Tk()
    g = GUI(root)
    root.mainloop()
