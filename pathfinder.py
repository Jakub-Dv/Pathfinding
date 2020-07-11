from map_generator import Map



def find_path(map):

    start = map.start
    end = map.end
    return AStar(map.map, start, end)


def AStar(map, start, end):
    closed_set = []
    open_set = [start]
    g_score = {start: 0}
    h_score = {start: distance(start, end)}
    f_score = {start: h_score[start] + g_score[start]}
    come_from = {}

    while open_set is not []:
        if not f_score:
            break

        l = list(f_score.values())
        l.sort()
        smallest_value = l[0]

        for k, v in f_score.items():
            if k in open_set and smallest_value == v:
                smallest_f = k
        if smallest_f == end:
            return final_path(come_from, start, end)

        if smallest_f in open_set:
            open_set.pop(open_set.index(smallest_f))
            del f_score[smallest_f]
        if not smallest_f in closed_set:
            closed_set.append(smallest_f)

        for neigh in neighbours(smallest_f, map):
            if neigh in closed_set:
                continue
            current_g_score = g_score[smallest_f] + distance(smallest_f, neigh)
            #print(f'{neigh} => {smallest_f}: {current_g_score}')

            if not neigh in open_set:
                open_set.append(neigh)
                g_score[neigh] = g_score[smallest_f] + distance(smallest_f, neigh)
                h_score[neigh] = distance(neigh, end)
                f_score[neigh] = g_score[neigh] + h_score[neigh]
                current_is_better = True
            elif current_g_score < g_score[neigh]:
                current_is_better = True
            else:
                current_is_better = False

            if current_is_better:
                #print('Is better')
                come_from[neigh] = smallest_f
                g_score[neigh] = current_g_score
                h_score[neigh] = distance(neigh, end)
                f_score[neigh] = g_score[neigh] + h_score[neigh]
        #print(come_from)

    return ValueError('No path exists')



def final_path(come_from, start, end):
    path = []
    while end != start:
        path.append(end)
        end = come_from[end]

    return path


def neighbours(current, map):
    current = list(current)
    l = len(map[0])
    if current[0] - 1 >= 0 and map[current[0] - 1][current[1]]:
        yield current[0] - 1, current[1]
    #if current[0] - 1 >= 0 and current[1] - 1 >= 0 and map[current[0] - 1][current[1] - 1]:
        #yield current[0] - 1, current[1] - 1
    if current[1] - 1 >= 0 and map[current[0]][current[1] - 1]:
        yield current[0], current[1] - 1
    #if current[0] + 1 < l and current[1] - 1 >= 0 and map[current[0] + 1][current[1] - 1]:
        #yield current[0] + 1, current[1] - 1
    if current[0] + 1 < l and map[current[0] + 1][current[1]]:
        yield current[0] + 1, current[1]
    #if current[0] + 1 < l and current[1] + 1 < l and map[current[0] + 1][current[1] + 1]:
        #yield current[0] + 1, current[1] + 1
    if current[1] + 1 < l and map[current[0]][current[1] + 1]:
        yield current[0], current[1] + 1
    #if current[0] - 1 >= 0 and current[1] + 1 < l and map[current[0] - 1][current[1] + 1]:
        #yield current[0] - 1, current[1] + 1


def distance(current, end):
    y_val = abs(list(current)[0] - list(end)[0])
    x_val = abs(list(current)[1] - list(end)[1])
    smaller = min(y_val, x_val)
    bigger = max(y_val, x_val)
    return smaller * 14 + (bigger - smaller) * 10


if __name__ == '__main__':
    map1 = Map(40, random=False)
