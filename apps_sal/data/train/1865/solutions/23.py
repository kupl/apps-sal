from heapq import *
class Solution:
    MOVES = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    def minPushBox(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == \"S\": playerPos = (i, j)
                if grid[i][j] == \"B\": boxPos = (i, j)
                if grid[i][j] == \"T\": targetPos = (i, j)
        
        steps = [[999999] * n for _ in range(m)]     # 记录从source/boxPos到(i, j)的步数，这个extra space在A*是必须的，用空间换时间
        steps[boxPos[0]][boxPos[1]] = 0
        
        hq = []
        visited = set()     # 其实A*算法里面也可以不用加visited, 因为每次都是朝曼哈顿最小的方向走的，很少会重复访问同一个节点，不像bfs会经常访问到同一个节点
        heappush(hq, (abs(boxPos[0]-targetPos[0]) + abs(boxPos[1]-targetPos[1]), 0, boxPos, playerPos)) 
        while hq:
            hueristicEstimation, step, currBoxPos, currPlayerPos = heappop(hq)
            if currBoxPos == targetPos:
                return steps[currBoxPos[0]][currBoxPos[1]]

            for move in self.MOVES:
                nextBoxPos_x, nextBoxPos_y = currBoxPos[0] + move[0], currBoxPos[1] + move[1]
                oppositeNextBoxPos_x, oppositeNextBoxPos_y = currBoxPos[0] - move[0], currBoxPos[1] - move[1]
                nextBoxPos = (nextBoxPos_x, nextBoxPos_y)
                oppositeNextBoxPos = (oppositeNextBoxPos_x, oppositeNextBoxPos_y)
                if nextBoxPos_x < 0 or nextBoxPos_x >= m or nextBoxPos_y < 0 or nextBoxPos_y >= n:
                    continue
                if grid[nextBoxPos_x][nextBoxPos_y] == \"#\":
                    continue
                if (nextBoxPos, currBoxPos) in visited:
                    continue
                if not self.playerCanReach(grid, currPlayerPos, oppositeNextBoxPos, currBoxPos):
                    continue
                heappush(hq, (step + abs(nextBoxPos[0]-targetPos[0]) + abs(nextBoxPos[1]-targetPos[1]), step + 1, nextBoxPos, currBoxPos)) 
                visited.add((nextBoxPos, currBoxPos))    # visited里面应该装入(boxPos, the pos where the boxPos comes from)
                steps[nextBoxPos[0]][nextBoxPos[1]] = step + 1
                    
        return -1
                    
    def playerCanReach(self, grid, startPos, endPos, boxPos):
        \"\"\"
        use manhatan distance as Heuristic esitimation for A-star algorithm: steps + (abs(nextPos[0]-endPos[0]) + abs(nextPos[1]-endPos[1])).  
        put the heuristic estimation in the hq, together with steps, so the hq stores 
        (heristic estimation of the minimum steps needed from source to target, steps, nextPos). 
        \"\"\"
        m, n = len(grid), len(grid[0])
        steps = [[999999] * n for _ in range(m)]     # 记录从source/boxPos到(i, j)的步数，这个extra space在A*是必须的，用空间换时间
        steps[startPos[0]][startPos[1]] = 0
        hq = []
        visited = set()
        heappush(hq, (abs(startPos[0] - endPos[0]) + abs(startPos[1] - endPos[1]), 0, startPos))
        visited.add(startPos)
        while hq:
            hueristicEstimation, step, currPos = heappop(hq)
            if currPos == endPos:
                return True
            for move in self.MOVES:
                nextPos_x, nextPos_y = currPos[0] + move[0], currPos[1] + move[1]
                nextPos = (nextPos_x, nextPos_y)
                if nextPos_x < 0 or nextPos_x >= m or nextPos_y < 0 or nextPos_y >= n:
                    continue
                if grid[nextPos_x][nextPos_y] == \"#\" or nextPos == boxPos:      # 易错点2: 遇到box的话也不能前进
                    continue
                if nextPos in visited:
                    continue
                heappush(hq, (step + abs(nextPos[0] - endPos[0]) + abs(nextPos[1] - endPos[1]), step + 1, nextPos))
                visited.add(nextPos)
                
        return False
