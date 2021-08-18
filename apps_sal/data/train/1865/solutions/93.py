class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        R, C = len(grid), len(grid[0])
        b_pos = s_pos = t_pos = None
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 'B':
                    b_pos = (r, c)
                if grid[r][c] == 'S':
                    s_pos = (r, c)
                if grid[r][c] == 'T':
                    t_pos = (r, c)

        def is_empty(r, c):
            return 0 <= r < R and 0 <= c < C and grid[r][c] != '

        visited = set()
        queue = [tuple(b_pos + s_pos)]
        steps = 0
        while queue:
            new_queue = []
            for br, bc, sr, sc in queue:
                new = (br, bc, sr, sc)
                if new in visited:
                    continue
                visited.add(new)
                if (br, bc) == t_pos:
                    return steps
                for dr, dc in dirs:
                    nsr, nsc = dr + sr, dc + sc
                    if (nsr, nsc) == (br, bc):
                        nbr, nbc = dr + br, dc + bc
                        box_move = True
                    else:
                        nbr, nbc = br, bc
                        box_move = False
                    if not is_empty(nsr, nsc) or not is_empty(nbr, nbc):
                        continue
                    new = (nbr, nbc, nsr, nsc)
                    if box_move:
                        new_queue.append(new)
                    else:
                        queue.append(new)
            queue = new_queue
            steps += 1
        return -1
