from random import choice


class Map:
    def __init__(self, size):
        self.map = [[choice((0, 0, 0, 0, 1)) for num in range(size)] for num in range(size)]
        self.map[0][0] = 'start'
        self.map[-1][-1] = 'end'

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

