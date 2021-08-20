class Solution:

    def minPushBox(self, grid: List[List[str]]) -> int:
        (rows, cols) = (len(grid), len(grid[0]))
        (br, bc) = (-1, -1)
        (sr, sc) = (-1, -1)
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 'B':
                    (br, bc) = (r, c)
                elif grid[r][c] == 'S':
                    (sr, sc) = (r, c)

        def reachable(br, bc, sr, sc, tr, tc):
            visited = {(sr, sc)}

            def helper(curr, curc):
                if curr == tr and curc == tc:
                    return True
                for (dr, dc) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    (newr, newc) = (curr + dr, curc + dc)
                    if newr < 0 or newr >= rows or newc < 0 or (newc >= cols):
                        continue
                    if grid[newr][newc] == '#' or (newr, newc) == (br, bc):
                        continue
                    if (newr, newc) in visited:
                        continue
                    visited.add((newr, newc))
                    if helper(newr, newc):
                        return True
                return False
            return helper(sr, sc)
        seen = {(br, bc, sr, sc)}
        step = 0
        frontier = [(br, bc, sr, sc)]
        while frontier:
            newft = []
            for (br, bc, sr, sc) in frontier:
                if grid[br][bc] == 'T':
                    return step
                for (dr, dc) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    (newr, newc) = (br + dr, bc + dc)
                    if newr < 0 or newr >= rows or newc < 0 or (newc >= cols):
                        continue
                    if grid[newr][newc] == '#':
                        continue
                    (targr, targc) = (br - dr, bc - dc)
                    if targr < 0 or targr >= rows or targc < 0 or (targc >= cols):
                        continue
                    if grid[targr][targc] == '#':
                        continue
                    if (newr, newc, targr, targc) in seen:
                        continue
                    if not reachable(br, bc, sr, sc, targr, targc):
                        continue
                    seen.add((newr, newc, targr, targc))
                    newft.append((newr, newc, targr, targc))
            step += 1
            frontier = newft
        return -1
