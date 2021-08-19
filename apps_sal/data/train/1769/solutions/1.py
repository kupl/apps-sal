def shortestPath(topology, startPoint, endPoint):
    (stack, shortest, paths) = ([(1, [startPoint])], float('inf'), [])
    while stack:
        (acc, path) = stack.pop()
        point = path[-1]
        if point == endPoint:
            if acc <= shortest:
                paths.append((acc, path))
                shortest = acc
            continue
        points = topology.get(point)
        for p in points:
            if p not in path:
                stack.append((acc + points[p] + 1, path + [p]))
    return sorted([path for (val, path) in paths if val == shortest])
