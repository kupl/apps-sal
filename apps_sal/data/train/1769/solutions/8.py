def find_all_paths(topology, start, end, path=[]):
    if start not in topology:
        return None
    path = path + [start]
    if start == end:
        return [path]

    paths = []
    for node in topology[start]:
        if node not in path:
            e_path = find_all_paths(topology, node, end, path)
            for p in e_path:
                paths.append(p)
    return paths


def distance(topology):
    dist = {}
    for element in topology:
        for node in topology[element]:
            dist[(element, node)] = topology[element][node]
    return dist


def calculate_path_distance(path, distances):
    path_dic = {}
    for p in path:
        d = 0
        for i in range(0, len(p) - 1):
            d = d + distances[tuple(p[i:i + 2])]
        path_dic[tuple(p)] = d
    return path_dic


def calculate_short_distance(paths_with_distance):
    shortest = []
    multiple_opt = {}
    shortest_opt = []
    values = sorted(paths_with_distance.values())
    for item in list(paths_with_distance.items()):
        if item[1] == values[0]:
            shortest.append(list(item[0]))
    if len(shortest) > 1:
        for i in shortest:
            multiple_opt[tuple(i)] = len(i)
        options = sorted(multiple_opt.values())
        for e in list(multiple_opt.items()):
            if e[1] == options[0]:
                shortest_opt.append(list(e[0]))
        shortest_opt.sort()
        return shortest_opt
    return shortest


def shortestPath(topology, start, end):
    path = find_all_paths(topology, start, end)
    distances = distance(topology)
    path_d = calculate_path_distance(path, distances)
    return calculate_short_distance(path_d)
