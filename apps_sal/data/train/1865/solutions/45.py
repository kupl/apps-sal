class Solution:
    def minPushBox(self, A: List[List[str]]) -> int:
        if not A: return -1

        rows, cols = len(A), len(A[0])
        box = end = dude = None
        
        for row in range(rows):
            for col in range(cols):
                if A[row][col] == 'B':   box = (row, col)
                elif A[row][col] == 'T': end = (row, col)
                elif A[row][col] == 'S': npc = (row, col)  
        
        def bfs(start, end, blocked):
            cache, q = set(start), collections.deque([start])
            while q:
                i, j = q.popleft()
                if (i, j) == end:
                    return True
                for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    row, col = i + di, j + dj
                    if 0 <= row < rows and 0 <= col < cols and \\
                       (row, col) not in cache and A[row][col] != '#' and \\
                       (row, col) != blocked:
                        q.append((row, col))
                        cache.add((row, col))
            return False
                
        visited, q = set([(box, npc)]), collections.deque([(box, npc, 0)])
        while q:
            (i, j), player, moves = q.popleft()
            if (i, j) == end:
                return moves
            for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                row, col = i + di, j + dj
                if 0 <= row < rows and 0 <= col < cols and ((row, col), (i, j)) not in visited and A[row][col] != '#':
                    if bfs(player, (i - di, j - dj), (i, j)):
                        q.append(((row, col), (i, j), moves + 1))
                        visited.add(((row, col), (i, j)))
        return -1
