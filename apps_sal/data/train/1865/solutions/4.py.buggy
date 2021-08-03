class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        
        def move(node, dx, dy):
            px, py, bx, by, dist = node
            px += dx
            py += dy
            illegal = (-1, -1, -1, -1, -1)
            if px < 0 or px >= m or py < 0 or py >= n or grid[px][py] == \"#\":
                return illegal
            if px == bx and py == by:
                bx += dx
                by += dy
                if bx < 0 or bx >= m or by < 0 or by >= n or grid[bx][by] == \"#\":
                    return illegal
                return (px, py, bx, by, dist+1)
            if grid[px][py] == \".\":
                return (px, py, bx, by, dist)
        
        player, target, box = [], [], []
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
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
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
                for dx, dy in directions:
                    newNode = move(node, dx, dy)
                    px2, py2, bx2, by2, dist2 = newNode
                    if newNode[0] != -1 and dist2 < visited[(px2, py2, bx2, by2)]:
                        queue.append(newNode)
                    
        
        return res if res < float(\"inf\") else -1
    
    
    
    
    
    
        
        
        
