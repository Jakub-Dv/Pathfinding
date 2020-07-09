from random import choice
from collections import defaultdict


class Map:
    def __init__(self, size, start=None, end=None, random=True):
        if start is None:
            start = (0, 0)
        if end is None:
            end = (size - 1, size - 1)

        if random:
            self.map = [[choice((1, 1, 1, 1, 1, 0, 0)) for num in range(size)] for num in range(size)]
        else:
            self.map = [[0 for num in range(size)] for num in range(size)]

        self.start = start
        self.end = end

    def __repr__(self):
        text = ''
        for block in self.map:
            for num in block:
                if num:
                    text += ' '
                else:
                    text += 'X'
            text += '\n'
        return text


def Maze_builder(size, start=None, end=None):

    grid = Map(size, start, end, random=False)
    fn(grid, grid.start)
    print(grid)


def fn(grid, current, opened=defaultdict(list), come_from=None):
    if come_from is None:
        come_from = {current: current}

    y, x = current
    grid.map[y][x] = 1
    print(grid)
    if opened.get(current) is None:
        for neigh in neighbours_for_maze(grid.map, current):
            if try_next(grid.map, current, neigh):
                opened[current].append(neigh)

    if not opened[current] == []:
        next_path = choice(opened[current])
        while not try_next(grid.map, current, next_path):
            next_path = choice(opened[current])
        come_from[next_path] = current
        for i, item in enumerate(opened[current]):
            if next_path == item:
                opened[current].pop(i)
                break

    else:
        next_path = come_from[current]
    print(f'{current}: {next_path}')
    if not next_path == current:
        fn(grid, next_path, opened, come_from)


def neighbours_for_maze(grid, position):
    y, x = position
    l = len(grid[0])
    if y - 1 >= 0 and grid[y - 1][x] == 0:
        yield y - 1, x
    if x - 1 >= 0 and grid[y][x - 1] == 0:
        yield y, x - 1
    if y + 1 < l and grid[y + 1][x] == 0:
        yield y + 1, x
    if x + 1 < l and grid[y][x + 1] == 0:
        yield y, x + 1


def try_next(grid, current, next_path):
    if next_path in neighbours_for_maze(grid, current) and grid[list(current)[0]][list(current)[1]] == 1:
        y, x = next_path
        if y == 0:
            if x == 0:
                if len(list(neighbours_for_maze(grid, next_path))) == 1:
                    return True
                return False
            elif x == len(grid[0]) - 1:
                if len(list(neighbours_for_maze(grid, next_path))) == 1:
                    return True
                return False
            else:
                if len(list(neighbours_for_maze(grid, next_path))) == 2:
                    return True
                return False

        elif x == 0:
            if y == len(grid[0]) - 1:
                if len(list(neighbours_for_maze(grid, next_path))) == 1:
                    return True
                return False
            else:
                if len(list(neighbours_for_maze(grid, next_path))) == 2:
                    return True
                return False

        elif y == len(grid[0]) - 1:
            if x == len(grid[0]) - 1:
                if len(list(neighbours_for_maze(grid, next_path))) == 1:
                    return True
                return False
            else:
                if len(list(neighbours_for_maze(grid, next_path))) == 2:
                    return True
                return False

        elif x == len(grid[0]) - 1:
            if len(list(neighbours_for_maze(grid, next_path))) == 2:
                return True
            return False

        else:
            if len(list(neighbours_for_maze(grid, next_path))) == 3:
                return True
            return False
    raise ValueError('Not a neighbour')


if __name__ == '__main__':
    Maze_builder(10)


