import heapq


def get_path(river):
    big_num = 10992312321
    nodes = []
    b = {}
    for y in range(len(river)):
        heapq.heappush(nodes, [river[y][0] * big_num, (y, 0)])
    while nodes[0][1][1] != len(river[0]) - 1:
        weight, node = heappop(nodes)
        ly, lx = node
        for dy, dx in [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]:
            if 0 <= ly + dy < len(river) and 0 <= lx + dx < len(river[0]) and (ly + dy, lx + dx) not in b:
                b[(ly + dy, lx + dx)] = (ly, lx)
                new_weight = max([weight // big_num, river[ly + dy][lx + dx]]) * big_num + weight % big_num + 1
                heapq.heappush(nodes, [new_weight, (ly + dy, lx + dx)])
    path = [nodes[0][1]]
    while path[-1][1] != 0:
        path.append(b[path[-1]])
    return nodes[0][0] // big_num, path


def shallowest_path(river):
    cost, path = get_path(river)
    for y in range(len(river)):
        for x in range(len(river[0])):
            if river[y][x] < cost:
                river[y][x] = 0
    cost, path = get_path(river)
    return path[::-1]
