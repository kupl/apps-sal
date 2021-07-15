class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        nrow, ncol = len(grid), len(grid[0])
        
        def move(tup, d):
            roffset, coffset = d
            pr,pc,br,bc,dist = tup
            pr += roffset
            pc += coffset
            illegal = (-1,-1,-1,-1,-1)
            if pr<0 or pr>=nrow or pc<0 or pc>= ncol or grid[pr][pc]==\"#\":
                return illegal
            if pr==br and pc==bc:
                br += roffset
                bc += coffset
                if br<0 or br>=nrow or bc<0 or bc>=ncol or grid[br][bc]==\"#\":
                    return illegal
                return (pr,pc,br,bc,dist+1)
            if grid[pr][pc] == \".\":
                return (pr,pc,br,bc,dist)
        
        p,t,b = [],[],[]
        for r in range(nrow):
            for c in range(ncol):
                if grid[r][c] == \"S\":
                    p = (r,c)
                    grid[r][c] = \".\"
                if grid[r][c] == \"T\":
                    t = (r,c)
                    grid[r][c] = \".\"
                if grid[r][c] == \"B\":
                    b = (r,c)
                    grid[r][c] = \".\"
                    
        q = collections.deque()
        q.append((p[0],p[1],b[0],b[1],0))
        visited = collections.defaultdict(lambda: float(\"inf\"))
        ret = float(\"inf\")
        while q:
            for _ in range(len(q)):
                tup = q.popleft()
                pr,pc,br,bc,dist = tup
                if (br,bc) == t:
                    ret = min(ret, dist)
                if dist < visited[(pr,pc,br,bc)]:
                    visited[(pr,pc,br,bc)] = dist
                else:
                    continue
                for d in [(-1,0),(1,0),(0,1),(0,-1)]:
                    tup2 = move(tup, d)
                    pr2,pc2,br2,bc2,dist2 = tup2
                    if pr2 != -1 and dist2 < visited[(pr2,pc2,br2,bc2)]:
                        q.append(tup2)
        return ret if ret < float(\"inf\") else -1
