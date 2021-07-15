class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        x,y,di=0,0,0
        dx=[0,1,0,-1]
        dy=[1,0,-1,0]
        obstacles=set(map(tuple,obstacles))
        ans=0
        
        for cmd in commands:
            if cmd==-2:
                di=(di-1)%4
            elif cmd==-1:
                di=(di+1)%4
            else:
                for k in range(cmd):
                    if (dx[di]+x,dy[di]+y) not in obstacles:
                        x+=dx[di]
                        y+=dy[di]
                        ans=max(ans,x**2+y**2)
        return ans
                

