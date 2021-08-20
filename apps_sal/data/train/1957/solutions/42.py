class Solution:

    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        (HT, WT) = (len(grid), len(grid[0]))
        TARGET = (HT - 1, WT - 1)
        from collections import deque
        q = deque([(0, 0, k)])
        visited = set(q)
        lvl_cnt = 0
        while q:
            for i in range(len(q)):
                (r, c, new_k) = q.popleft()
                if (r, c) == TARGET:
                    return lvl_cnt
                for (i, j) in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                    if 0 <= i < HT and 0 <= j < WT:
                        if grid[i][j] == 0 and (i, j, new_k) not in visited:
                            q.append((i, j, new_k))
                            visited.add((i, j, new_k))
                        elif grid[i][j] == 1 and new_k > 0 and ((i, j, new_k - 1) not in visited):
                            q.append((i, j, new_k - 1))
                            visited.add((i, j, new_k - 1))
            lvl_cnt += 1
        return -1
