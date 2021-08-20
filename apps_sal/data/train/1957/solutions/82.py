class Solution:

    def shortestPath(self, grid: List[List[int]], k: int) -> int:

        def method1():
            R = len(grid)
            if R < 1:
                return -1
            C = len(grid[0])
            seen = set()
            queue = collections.deque([(0, 0, k, 0)])
            seen.add((0, 0, k))

            def neighbors(r, c):
                for (dr, dc) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    (nr, nc) = (r + dr, c + dc)
                    if 0 <= nr < R and 0 <= nc < C:
                        yield (nr, nc)
            while queue:
                (r, c, K, dist) = queue.popleft()
                if r == R - 1 and c == C - 1:
                    return dist
                for (nr, nc) in neighbors(r, c):
                    if grid[nr][nc] == 1:
                        if K == 0:
                            continue
                        if (nr, nc, K - 1) in seen:
                            continue
                        seen.add((nr, nc, K - 1))
                        queue.append((nr, nc, K - 1, dist + 1))
                    else:
                        if (nr, nc, K) in seen:
                            continue
                        seen.add((nr, nc, K))
                        queue.append((nr, nc, K, dist + 1))
            return -1
        return method1()
