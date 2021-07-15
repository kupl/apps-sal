from queue import deque


class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        def isValid(pos):
            i, j = pos[0], pos[1]
            return 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] != '#'
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 'T':
                    target = (i, j)
                elif grid[i][j] == 'B':
                    box = (i, j)
                elif grid[i][j] == 'S':
                    player = (i, j)

        def personCanMove(pos, dest, box):
            que = deque([pos])
            seen = {pos}
            while que:
                p = que.popleft()
                if p == dest:
                    return True
                i, j = p[0], p[1]
                nextPos = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
                for nextI, nextJ in nextPos:
                    if isValid((nextI, nextJ)) and (nextI, nextJ) not in seen and (nextI, nextJ) != box:
                        seen.add((nextI, nextJ))
                        que.append((nextI, nextJ))
            return False
        q = deque([(box, player, 0)])
        seen = {box + player}
        while q:
            b, p, pushes = q.popleft()
            if b == target:
                return pushes
            nextBArr = [(b[0]-1, b[1]), (b[0]+1, b[1]),
                        (b[0], b[1]+1), (b[0], b[1]-1)]
            pushPosArr = [(b[0]+1, b[1]), (b[0]-1, b[1]),
                          (b[0], b[1]-1), (b[0], b[1]+1)]
            for nextB, pushPos in zip(nextBArr, pushPosArr):
                if isValid(nextB) and nextB+b not in seen:
                    if isValid(pushPos) and personCanMove(p, pushPos, b):
                        q.append((nextB, b, pushes + 1))
                        seen.add(nextB + b)
        return -1

