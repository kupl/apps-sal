from collections import deque, namedtuple

Step = namedtuple('Step', [\"row\", \"col\", \"step\"])

class Solution:
    def shortestPath(self, m: List[List[int]], k: int) -> int:
        queue = deque()
        queue.append(Step(row=0,col=0,step=0))
        visited = set([Step(row=0,col=0,step=0)])

        level = 0

        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        destX, destY = len(m) - 1, len(m[0]) - 1

        while len(queue):
            for _ in range(len(queue)):
                posX, posY, step = queue.popleft()
                if (posX, posY) == (destX, destY):
                    return level
                for x, y in directions:
                    newX, newY = x + posX, y + posY
                    if (0 <= newX < len(m)) and (0 <= newY < len(m[0])):

                        if m[newX][newY] == 1:
                            new_step = step + 1
                            next_move = Step(row=newX,col=newY,step=new_step)
                            if next_move not in visited and new_step <= k:
                                queue.append(next_move)
                                visited.add(next_move)
                        else:
                            next_move = Step(row=newX,col=newY,step=step)
                            if next_move not in visited:
                                queue.append(next_move)
                                visited.add(next_move)
            level += 1

        return -1
        
