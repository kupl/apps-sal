class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        q=collections.deque([[0,0,k]])
        res,m,n=0,len(grid),len(grid[0])
        seen=set()
        dirs=[[0,1],[0,-1],[1,0],[-1,0]]
        while q:
            for i in range(len(q)):
                cur=q.popleft()
                if cur[0]==m-1 and cur[1]==n-1:
                    return res
                for di in dirs:
                    ni=cur[0]+di[0]
                    nj=cur[1]+di[1]
                    if ni<0 or ni>=m or nj<0 or nj>=n:
                        continue
                    ha=str(ni)+\",\"+str(nj)+\",\"+str(cur[2])
                    if ha not in seen:
                        if grid[ni][nj]==0:
                            seen.add(ha)
                            q.append([ni,nj,cur[2]])
                        else:
                            if cur[2]>0:
                                seen.add(ha)
                                q.append([ni,nj,cur[2]-1])
            res+=1
            
        return -1
            
