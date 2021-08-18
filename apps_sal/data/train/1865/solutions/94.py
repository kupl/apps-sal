import heapq


class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 'S':
                    s = (i, j)
                if grid[i][j] == 'B':
                    b = (i, j)
                if grid[i][j] == 'T':
                    t = (i, j)

        def valid(i, j, s=None, b=None):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
                return False
            if grid[i][j] == '
            return False
            if s is not None:
                if (i, j) == s:
                    return False
            if b is not None:
                if (i, j) == b:
                    return False
            return True

        def next_state(s, b, step):
            for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                if valid(s[0] + di, s[1] + dj):
                    if b == (s[0] + di, s[1] + dj) and valid(b[0] + di, b[1] + dj):
                        nxt_s, nxt_b, nxt_step = b, (b[0] + di, b[1] + dj), step + 1
                    else:
                        nxt_s = (s[0] + di, s[1] + dj)
                        nxt_b, nxt_step = b, step
                    yield nxt_s, nxt_b, nxt_step

        def edit_dis(s, b):
            return abs(s[0] - b[0]) + abs(s[1] - b[1])

        def search(s, b):
            q = [(0, edit_dis(s, b), s, b)]
            visited = {}
            visited[(s, b)] = 0
            while q:
                (step, _, s, b) = heapq.heappop(q)
                if b == t:
                    return step
                for nxt_s, nxt_b, nxt_step in next_state(s, b, step):
                    if (nxt_s, nxt_b) not in visited or visited[(nxt_s, nxt_b)] > nxt_step:
                        q.append((nxt_step, edit_dis(nxt_s, nxt_b), nxt_s, nxt_b))
                        visited[(nxt_s, nxt_b)] = nxt_step
            return -1
        return search(s, b)
