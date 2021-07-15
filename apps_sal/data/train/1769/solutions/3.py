from collections import defaultdict, deque    #using dijkstra
def shortestPath(topology, start, end):
    vertices = defaultdict(list)
    edges, distance_, parent_ = {}, {}, {}
    
    for i, j in topology.items():
        distance_[i] = float('inf')
        parent_[i] = None
        for k, l in j.items():
            vertices[i].append(k)
            edges[(i, k)] = l
    
    distance_[start] = 0
    Q = deque([[(start, 0), distance_, parent_]])
    pairs, PATHS = set(), set()
    while Q:
        (node, cost), distance, parent = Q.popleft()
        while distance:
            if node == end : break
            for neighbour in vertices[node]:
                if neighbour in distance:
                    dis = cost + edges[(node, neighbour)]
                    if dis < distance[neighbour]:
                        distance[neighbour] = dis
                        parent[neighbour] = node
    
            del distance[node]
            node, cost = min(distance.items(), key=lambda x: x[1])
            for i, j in distance.items():
                if (i, node) not in pairs and j == cost and i != node:
                    pairs.add((i, node))
                    Q.append([(i, j), distance.copy(), parent.copy()])
        
        path, node = [], end
        while node != start:
            path.insert(0, node)
            node = parent[node]
    
        PATHS.add((start,) + tuple(path))
    
    return sorted(list(map(list,PATHS)))
