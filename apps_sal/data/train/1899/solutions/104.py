class Solution:

    def shortestBridge(self, A: List[List[int]]) -> int:
        count = 0
        borders = collections.defaultdict(list)
        seen = set()
        (x, y) = ([1, -1, 0, 0], [0, 0, 1, -1])
        (m, n) = (len(A), len(A[0]))
        for i in range(m):
            for j in range(n):
                if A[i][j] == 1 and (i, j) not in seen:
                    frontier = [(i, j)]
                    island = {(i, j)}
                    while frontier:
                        cur = frontier.pop()
                        bord = False
                        for k in range(len(x)):
                            (r, c) = (cur[0] + x[k], cur[1] + y[k])
                            if 0 <= r < m and 0 <= c < n:
                                if A[r][c] == 1 and (r, c) not in island:
                                    frontier.append((r, c))
                                    island.add((r, c))
                                elif A[r][c] == 0:
                                    borders[count + 1].append(cur)
                    count += 1
                    seen.update(island)
                if count == 2:
                    break
            if count == 2:
                break
        ans = float('inf')
        borders
        for (i, j) in borders[1]:
            for (x, y) in borders[2]:
                ans = min(ans, abs(i - x) + abs(j - y) - 1)
        return ans
