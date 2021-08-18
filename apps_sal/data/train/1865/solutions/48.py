class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        R, C = len(grid), len(grid[0])

        def nxt(pos):
            r, c = pos
            res = []
            for nr, nc in [[r + 1, c], [r, c + 1], [r - 1, c], [r, c - 1]]:
                if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] != '
                res.append((nr, nc))
            return res

        def connected(p, q, box):
            queue = collections.deque([p])
            seen = set()
            while queue:
                node = queue.popleft()
                for nr, nc in nxt(node):
                    if (nr, nc) != box:
                        if (nr, nc) == q:
                            return True
                        if (nr, nc) not in seen:
                            seen.add((nr, nc))
                            queue.append((nr, nc))
            return False

        target, box, worker = None, None, None

        for r in range(R):
            for c in range(C):
                if grid[r][c] == 'S':
                    worker = (r, c)
                if grid[r][c] == 'B':
                    box = (r, c)
                if grid[r][c] == 'T':
                    target = (r, c)

        level = []
        seen = set()
        for pos in nxt(box):
            if connected(pos, worker, box):
                level.append((box, pos))
                seen.add((box, pos))

        grid[box[0]][box[1]] = '.'
        steps = 0

        while level:
            n_level = []
            for b, w in level:
                candi = nxt(b)
                for pos in candi:
                    nb = (2 * b[0] - pos[0], 2 * b[1] - pos[1])
                    if nb == target:
                        return steps + 1
                    if nb in candi and (nb, b) not in seen and connected(w, pos, b):
                        seen.add((nb, b))
                        n_level.append((nb, b))
            steps += 1
            level = n_level

        return -1
