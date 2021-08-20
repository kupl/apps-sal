class Solution:

    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        (R, C) = (len(grid), len(grid[0]))
        if R == 1 and C == 1:
            return 0
        if k >= R - 1 + C - 1:
            return R - 1 + C - 1
        q = collections.deque([(0, 0, k, 0)])
        seen = set([(0, 0, k)])
        while q:
            (i, j, left, steps) = q.popleft()
            for (new_i, new_j) in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= new_i < R and 0 <= new_j < C:
                    if grid[new_i][new_j] == 1 and left > 0 and ((new_i, new_j, left - 1) not in seen):
                        seen.add((new_i, new_j, left - 1))
                        q.append((new_i, new_j, left - 1, steps + 1))
                    elif grid[new_i][new_j] == 0 and (new_i, new_j, left) not in seen:
                        if new_i == R - 1 and new_j == C - 1:
                            return steps + 1
                        seen.add((new_i, new_j, left))
                        q.append((new_i, new_j, left, steps + 1))
        return -1
