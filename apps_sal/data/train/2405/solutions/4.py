class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        d = 0
        x, y = 0, 0
        
        oset = set()
        for o in obstacles: 
            oset.add(tuple(o))
        
        result = 0
        for c in commands: 
            if c == -1:
                d = (d + 1)% 4
            elif c == -2: 
                d = (d + 4 - 1)%4
            else: 
                for k in range(c): 
                    if (x + dx[d], y + dy[d]) not in oset: 
                        x+= dx[d]
                        y += dy[d]
                        result = max(result, x*x + y*y)
        return result

