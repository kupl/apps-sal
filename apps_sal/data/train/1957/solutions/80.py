class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        def method1():
            R = len(grid)
            if R < 1:
                return -1
            C = len(grid[0])
            seen = set()
            queue = collections.deque([(0, 0, k, 0)])  # r,c,k,dist
            seen.add((0, 0, k))

            def neighbors(r, c):
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < R and 0 <= nc < C):
                        yield nr, nc

            while queue:
                r, c, ck, dist = queue.popleft()
                if r == R - 1 and c == C - 1:
                    return dist

                for nr, nc in neighbors(r, c):
                    newk = ck
                    if grid[nr][nc] == 1:
                        newk -= 1
                        if newk < 0:
                            continue
                    if (nr, nc, newk) in seen:
                        continue
                    seen.add((nr, nc, newk))
                    queue.append((nr, nc, newk, dist + 1))

            return -1
        return method1()
