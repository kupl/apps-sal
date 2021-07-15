import sys
from collections import deque
import gc


def findCycle(source, getNbr):
    q = deque([source])
    parent = {source: None}
    while q:
        node = q.popleft()
        for nbr in getNbr(node):
            if nbr not in parent:
                q.append(nbr)
                parent[nbr] = node
            else:
                cycle = [node]
                while parent[node] != nbr:
                    node = parent[node]
                    cycle.append(node)
                cycle.append(nbr)
                return cycle[::-1]


def markTime(cycle, getNbr):
    cycleLen = len(cycle)
    q = deque(cycle)
    dist = {x: cycleLen - 1 - i for i, x in enumerate(cycle)} # distance to reach cycle[-1]
    while q:
        node = q.popleft()
        d = dist[node]
        for nbr in getNbr(node):
            if nbr not in dist:
                q.append(nbr)
                dist[nbr] = (d + 1) % cycleLen
    return dist


def solve(R, C, grid, directions):
    BLACK = 0
    drdc = {
        "U": [-1, 0],
        "R": [0, 1],
        "D": [1, 0],
        "L": [0, -1],
    }

    def getNbr(i):
        r, c = divmod(i, C)
        dr, dc = drdc[directions[r][c]]
        return [(r + dr) * C + (c + dc)]

    def getNbrT(i):
        r, c = divmod(i, C)
        ret = []
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < R and 0 <= nc < C:
                if [-dr, -dc] == drdc[directions[nr][nc]]:
                    ret.append(nr * C + nc)
        return ret

    ans1 = 0
    ans2 = 0
    seen = set()
    for i in range(R * C):
        if i not in seen:
            # BFS until found cycle
            cycle = findCycle(i, getNbr)
            uniqueTimes = len(cycle)
            # Find all nodes going to cycle
            # Each starting node going into cycle will have a collision timestamp mod cycle len
            dist = markTime(cycle, getNbrT)
            uniqueBlackTimes = set()
            for j, t in list(dist.items()):
                r, c = divmod(j, C)
                if grid[r][c] == BLACK:
                    uniqueBlackTimes.add(t)
                seen.add(j)
            ans1 += uniqueTimes
            ans2 += len(uniqueBlackTimes)
            del cycle
            del dist
            del uniqueBlackTimes

    return str(ans1) + " " + str(ans2)


def __starting_point():
    input = sys.stdin.readline

    T = int(input())
    for t in range(T):
        R, C = [int(x) for x in input().split()]
        grid = [list(map(int, input().rstrip())) for r in range(R)]
        directions = [list(input().rstrip()) for r in range(R)]

        ans = solve(R, C, grid, directions)
        print(ans)

__starting_point()
