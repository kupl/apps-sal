class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        gather = []
        for y in range(len(A)):
            for x in range(len(A[y])):
                if A[y][x] == 1:
                    A[y][x] = 2
                    gather.append((x, y, 0))
                    break
            if gather:
                break

        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        seen = set([gather[0]])
        while gather:
            frontier = []
            for x, y, _ in gather:
                for dx, dy in dirs:
                    xx, yy = x + dx, y + dy
                    if (xx, yy, 0) in seen:
                        continue
                    if 0 <= yy < len(A) and 0 <= xx < len(A[yy]) and A[yy][xx] == 1:
                        A[yy][xx] = 2
                        seen.add((xx, yy, 0))
                        frontier.append((xx, yy, 0))
            gather = frontier

        bfs = list(seen)
        while bfs:
            frontier = []
            for x, y, n in bfs:
                A[y][x] = 2
                for dx, dy in dirs:
                    xx, yy = x + dx, y + dy
                    if 0 <= yy < len(A) and 0 <= xx < len(A[yy]):
                        if A[yy][xx] == 1:
                            return n
                        elif A[yy][xx] == 0:
                            A[yy][xx] = 2
                            frontier.append((xx, yy, n + 1))
            bfs = frontier

        return -1
