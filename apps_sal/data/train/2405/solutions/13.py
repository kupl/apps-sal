class Solution:

        
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        gldis=0
        pos=[0,0]
        dr=0
        obs={tuple(i) for i in obstacles}
        def nex (dr):
            if dr==0:
                return [pos[0],pos[1]+1]
            if dr==1:
                return [pos[0]+1,pos[1]]
            if dr==2:
                return [pos[0],pos[1]-1]
            if dr==3:
                return [pos[0]-1,pos[1]]
        for i in commands:
            if i==-1:
                ne=dr+1
                dr=ne%4
            if i==-2:
                ne=dr-1
                dr=ne%4
            else: 
                j=0
                while j<i and (tuple(nex(dr)) not in obs):
                        pos=nex(dr)
                        j+=1
                gldis=max(gldis,pos[0]*pos[0]+pos[1]*pos[1])
        return gldis
            
                

