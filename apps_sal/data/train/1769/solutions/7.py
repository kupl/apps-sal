def shortestPath(topology, startPoint, endPoint):
    graph = {}
    for (key, value) in topology.items():
        values = []
        for (k, v) in value.items():
            values.append(k)
        graph[key] = values
    paths = find_all_paths(graph, startPoint, endPoint)
    if len(paths) == 0:
        return []
    pathsAndDistances = []
    for path in paths:
        distance = 0
        for (i, waypoint) in enumerate(path):
            if i < len(path) - 1:
                distance += topology[waypoint][path[i + 1]]
        pathsAndDistances.append((distance, path))
    pathsAndDistances = [t for t in pathsAndDistances if t[0] == min(pathsAndDistances)[0]]
    length = 1000
    for p in pathsAndDistances:
        if len(p[1]) < length:
            length = len(p[1])
    answer = []
    for p in pathsAndDistances:
        if len(p[1]) == length:
            answer.append(p[1])
    return answer


def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths
