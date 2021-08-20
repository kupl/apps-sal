class Solution:

    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        (R, C) = (len(grid), len(grid[0]))
        if R == 1 and C == 1:
            return 0
        cur = [(0, 0, 0, k)]
        step = 0
        seen = {(0, 0): k}
        while cur:
            nex = []
            for (s, r, c, remain) in cur:
                for (rp, cp) in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                    if 0 <= rp < R and 0 <= cp < C:
                        if rp == R - 1 and cp == C - 1:
                            return s + 1
                        next_remain = remain if grid[rp][cp] == 0 else remain - 1
                        if next_remain < 0:
                            continue
                        if seen.get((rp, cp), -1) < next_remain:
                            seen[rp, cp] = next_remain
                            nex.append((s + 1, rp, cp, next_remain))
            cur = nex
        return -1
