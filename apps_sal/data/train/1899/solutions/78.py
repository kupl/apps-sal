class Solution:
    def shortestBridge(self, mat: List[List[int]]) -> int:
        R = len(mat)
        C = len(mat and mat[0])

        def expand(island, other):
            new = set()
            for r, c in island:
                for nr, nc in (r + 1, c), (r, c + 1), (r - 1, c), (r, c - 1):
                    if R > nr >= 0 <= nc < C:
                        if (nr, nc) in other:
                            return True
                        if mat[nr][nc] == 0:
                            mat[nr][nc] = 2
                            new.add((nr, nc))
            island.update(new)

        def findIsland(r, c, island):
            island.add((r, c))
            mat[r][c] = 2
            for nr, nc in (r + 1, c), (r, c + 1), (r - 1, c), (r, c - 1):
                if R > nr >= 0 <= nc < C and mat[nr][nc] == 1:
                    findIsland(nr, nc, island)

        islands = []
        for r in range(R):
            for c in range(C):
                if mat[r][c] == 1:
                    island = set()
                    findIsland(r, c, island)
                    islands.append(island)

        ans = 0
        while True:
            if expand(*islands):
                return ans
            ans += 1
            islands = islands[::-1]
