class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        
        def move(tup, d):
            roffset, coffset = d
            pr, pc, br, bc, dist = tup
            pr += roffset
            pc += coffset
            illegal = (-1, -1, -1, -1, -1)
            if pr < 0 or pr >= m or pc < 0 or pc >= n or grid[pr][pc] == \"#\":
                return illegal
            if pr == br and pc == bc:
                br += roffset
                bc += coffset
                if br < 0 or br >= m or bc < 0 or bc >= n or grid[br][bc] == \"#\":
                    return illegal
                return (pr, pc, br, bc, dist+1)
            if grid[pr][pc] == \".\":
                return (pr, pc, br, bc, dist)
        
        player, t, b = [], [], []
        for r in range(m):
            for c in range(n):
                if grid[r][c] == \"S\":
                    player = (r, c)
                    grid[r][c] = \".\"
                if grid[r][c] == \"T\":
                    target = (r, c)
                    grid[r][c] = \".\"
                if grid[r][c] == \"B\":
                    box = (r, c)
                    grid[r][c] = \".\"
        
        queue = collections.deque()
        queue.append((player[0], player[1], box[0], box[1], 0))
        visited = collections.defaultdict(lambda: float(\"inf\"))
        res = float(\"inf\")
        while queue:
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                px, py, bx, by, dist = node
                if (bx, by) == target:
                    res = min(res, dist)
                if dist < visited[(px, py, bx, by)]:
                    visited[(px, py, bx, by,)] = dist
                else:
                    continue
                for d in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    newNode = move(node, d)
                    px2, py2, bx2, by2, dist2 = newNode
                    if newNode[0] != -1 and dist2 < visited[(px2, py2, bx2, by2)]:
                        queue.append(newNode)
                    
        
        return res if res < float(\"inf\") else -1
    
    
    
    
    
    
        
        
        
