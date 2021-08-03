from time import time
class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        
        d = dict()
        
        lim1 = len(grid)
        lim2 = len(grid[0])
        
        for i in range(0,lim1):
            for j in range(0,lim2):
                if grid[i][j]!=\"#\":
                    val = (i,j)
                    d[val]=[]
                    if i>0 and grid[i-1][j]!=\"#\":
                        d[val].append((i-1,j))
                    if j>0 and grid[i][j-1]!=\"#\":
                        d[val].append((i,j-1))
                    if i<lim1-1 and grid[i+1][j]!=\"#\":
                        d[val].append((i+1,j))
                    if j<lim2-1 and grid[i][j+1]!=\"#\":
                        d[val].append((i,j+1))
                        
                    if grid[i][j]=='S':
                        start = (i,j)
                    elif grid[i][j]=='T':
                        target = (i,j)
                    elif grid[i][j]=='B':
                        box = (i,j)
        mx = max(lim1,lim2)
        def gotobox(c1,c2,b):
            arr = [[-1 for i in range(0,mx)] for j in range(0,mx)]
            arr[c1[0]][c1[1]]=1
            f = []
            begin = [c1]
            while 1!=-1:
                cache = []
                ###print(f)
                for x in begin:
                    if x in c2 and x not in f:
                        
                        f.append(x)
                        
                        
                    for y in d[x]:
                        
                        ###if y==(2,2):print(1)
                        if y!=b and arr[y[0]][y[1]]==-1:
                            arr[y[0]][y[1]]=1
                            cache.append(y)
                ###print(cache,c2)
                if cache==[]:
                    
                    return f
                
                begin = cache
        arr2 = [[[[-1 for i in range(0,mx)] for j in range(0,mx)] for a in range(0,mx)] for b in range(0,mx)]    
        
        tmp1 = [[start,box,0]]
        while 1!=-1:
            
            tmp2 = []
            
            for x in tmp1:
                
                if arr2[x[0][0]][x[0][1]][x[1][0]][x[1][1]]==-1:
                    arr2[x[0][0]][x[0][1]][x[1][0]][x[1][1]]=1
                    for y in d[x[0]]:

                        if x[1]==target:

                            return x[-1]
                        else:
                            vals = gotobox(x[0],d[x[1]],x[1])

                            if vals ==-1:return -1

                            for z in vals:
                                for a in d[x[1]]:

                                    if (z[0]==a[0] and z[1]==a[1]+2) or (z[0]==a[0] and z[1]==a[1]-2) or (z[1]==a[1] and z[0]==a[0]+2) or (z[1]==a[1] and z[0]==a[0]-2): tmp2.append([z,a,x[2]+1])
                    
                        
            if tmp2==[]:return -1
            tmp1 = tmp2
     
                                
                        
                        
            
