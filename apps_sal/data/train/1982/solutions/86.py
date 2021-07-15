class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        c=[-1 for i in range(N)]
        if(len(dislikes)==0):
            return True
        dislikes.sort()
        el=[[] for i in range(N)]
        for i in dislikes:
            el[i[0]-1].append(i[1]-1)
            el[i[1]-1].append(i[0]-1)
        x=dislikes[0][0]
        vis=[i for i in range(N)]
        vis.remove(x)
        c[x]=0
        d=[x]
        while(d!=[]):
            f=[]
            for i in d:
                for j in el[i]:
                    if(c[j]==-1):
                        vis.remove(j)
                        c[j]=1-c[i]
                        f.append(j)
                    elif(c[j]!=1-c[i]):
                        return False
                    else:
                        continue
            d=f
            if(d==[])and(len(vis)!=0):
                d=[vis.pop()]
                c[d[0]]=0
        return True
                    

