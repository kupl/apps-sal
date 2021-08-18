class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        def method1():
            R = len(grid)
            if R < 1:
                return 0
            C = len(grid[0])

            def neighbors(r, c):
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < R and 0 <= nc < C:
                        yield nr, nc

            def dfs(r, c, visited):
                if (r, c) in seen:
                    return

                if grid[r][c] == 0:
                    return

                seen.add((r, c))
                visited.add((r, c))
                for nr, nc in neighbors(r, c):
                    dfs(nr, nc, visited)

            ans = float('-inf')
            seen = set()
            cc = []
            zeros = set()

            for r in range(R):
                for c in range(C):
                    if grid[r][c] == 1 and (r, c) not in seen:
                        visited = set()
                        dfs(r, c, visited)
                        if visited:
                            cc.append(visited)

                    if grid[r][c] == 0:
                        zeros.add((r, c))

            if len(zeros) == R * C:
                return 1

            ans = len(max(cc, key=len))
            for r, c in zeros:
                nei = {(nr, nc) for nr, nc in neighbors(r, c)}

                if len(cc) == 1:
                    if any((r, c) in cc[0] for r, c in nei):
                        ans = max(ans, len(cc[0]) + 1)
                else:
                    for i in range(len(cc)):
                        for j in range(i, len(cc)):
                            if (i != j and any((r, c) in cc[i] for r, c in nei) and any((r, c) in cc[j] for r, c in nei)):
                                ans = max(ans, len(cc[i]) + len(cc[j]) + 1)

            return ans

        def method2():
            R = len(grid)
            if R < 1:
                return 0
            C = len(grid[0])

            def neighbors(r, c):
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < R and 0 <= nc < C:
                        yield nr, nc

            def dfs(r, c, index):
                ans = 1
                grid[r][c] = index
                for nr, nc in neighbors(r, c):
                    if grid[nr][nc] == 1:
                        ans += dfs(nr, nc, index)
                return ans

            area = {}
            index = 2
            for r in range(R):
                for c in range(C):
                    if grid[r][c] == 1:
                        area[index] = dfs(r, c, index)
                        index += 1

            ans = max(list(area.values()) or [0])
            for r in range(R):
                for c in range(C):
                    if grid[r][c] == 0:
                        seen = {grid[nr][nc] for nr, nc in neighbors(r, c) if grid[nr][nc] > 1}
                        ans = max(ans, 1 + sum(area[i] for i in seen))

            return ans
        return method2()
