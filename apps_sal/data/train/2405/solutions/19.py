class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        arrow = [(-1,0), (0,1), (1,0), (0,-1)]
        arrowNow = 1
        curPoint = [0,0]
        obstacles = [tuple(e) for e in obstacles]
        setObs = set(obstacles)
        ans = 0
        for e in commands:
            if e==-1:
                arrowNow= (arrowNow+1)%4
            elif e==-2:
                arrowNow= (arrowNow-1)%4
            else:
                for i in range(e):
                    rowNow = curPoint[0] + arrow[arrowNow][0]
                    colomNow = curPoint[1] + arrow[arrowNow][1]
                    if (rowNow, colomNow) not in setObs:
                        ans = max(ans, rowNow**2 + colomNow**2)
                        curPoint[0], curPoint[1] = rowNow, colomNow
        return ans
        
                        

