import heapq

def knight(p1, p2):
    heuristic = lambda f: max(abs(f[0] - p2[0]), abs(f[1] - p2[1])) // 2
    p1, p2 = ((ord(p[0]) - ord('a'), int(p[1]) - 1) for p in (p1, p2))
    pqueue = [(heuristic(p1), p1, 0)]
    while pqueue:
        _, (x, y), count = heapq.heappop(pqueue)
        if (x, y) == p2:
            return count
        for dx, dy in ((-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)):
            x2, y2 = x + dx, y + dy
            if 0 <= x2 < 8 and 0 <= y2 < 8:
                heapq.heappush(pqueue, (count + heuristic((x2, y2)), (x2, y2), count + 1))
