class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        walls = set()
        for i in range(-1, n+1):
            for j in [-1,m]:
                walls.add(i + j *1j)
        for i in [-1,n]:
            for j in range(-1, m+1):
                walls.add(i + j *1j)

        for i, row in enumerate(grid):
            for j, c in enumerate(row):
                if c == \"S\":
                    spos = i + j * 1j
                elif c == \"T\":
                    tpos = i + j * 1j
                elif c == \"B\":
                    bpos = i + j * 1j
                elif c == \"#\":
                    walls.add(i + j * 1j)
        
        def children(node):
            return [node + x for x in [1,-1,1j,-1j]]
        
        def connected(pos1, pos2, bpos):
            q = [pos1]
            seen = set(q)
            while q:
                node = q.pop(0)
                if node == pos2: return True
                for child in children(node):
                    if child in walls or child == bpos: continue
                    if child in seen: continue
                    seen.add(child)
                    q.append(child)
            return False
        
        depth = {(spos, bpos): 0}
        
        q = [(spos, bpos)]
        while q:
            spos, bpos = q.pop(0)
            if bpos == tpos:
                return depth[(spos, bpos)]
            for child in children(bpos):
                if child in walls: continue
                newspos = 2*bpos - child
                if newspos in walls: continue
                if not connected(spos, newspos, bpos): continue
                if (newspos, child) in depth: continue
                depth[(newspos, child)] = depth[(spos, bpos)] + 1
                q.append((newspos, child))
        return -1

