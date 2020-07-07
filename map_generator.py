from random import choice


class Map:
    def __init__(self, size, start=(0, 0), end=None):
        if end is None:
            end = (size - 1, size - 1)
        self.map = [[choice((1, 1, 1, 1, 0, 0)) for num in range(size)] for num in range(size)]
        self.map[0][0] = 'start'
        self.map[-1][-1] = 'end'
        self.start = start
        self.end = end

    def __repr__(self):
        text = ''
        for block in self.map:
            for num in block:
                if num:
                    text += 'X'
                else:
                    text += ' '
            text += '\n'
        return text


if __name__ == '__main__':
    map1 = Map(50)
    print(map1)

