import queue


def shortestPath(topology, startPoint, endPoint):
    q = queue.Queue()
    q.put([startPoint, [startPoint], 0])
    routes = []

    while not q.empty():
        current_node, path, cost = q.get()
        if current_node == endPoint:
            routes.append((path, cost))
        for point, distance in list(topology[current_node].items()):
            new_path = path.copy()
            if point not in path:
                new_path += [point]
                q.put([point, new_path, cost + topology[current_node][point]])
    lowest_cost = min(routes, key=lambda x: x[1])
    other_lowest_cost = [x[0] for x in routes if x[1] == lowest_cost[1] and len(x[0]) == len(lowest_cost[0])]
    return other_lowest_cost
