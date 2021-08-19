Offsets = ((-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2))


def knights_tour(start, size):
    visited = {}
    peers = {}
    path = [start]
    for y in range(size):
        for x in range(size):
            visited[y, x] = 0
            peers[y, x] = [(oy + y, ox + x) for (oy, ox) in Offsets if 0 <= oy + y < size and 0 <= ox + x < size]
    size **= 2
    visited[start] = 1

    def find(curr):
        if len(path) == size:
            return path
        for peer in sorted((p for p in peers[curr] if not visited[p]), key=lambda p: sum((not visited[p2] for p2 in peers[p]))):
            visited[peer] = 1
            path.append(peer)
            if find(peer):
                return path
            visited[peer] = 0
            path.pop()
    return find(start)
