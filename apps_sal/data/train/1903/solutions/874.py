class Subsets:
    def __init__(self,parent,rank):
        self.parent=parent
        self.rank=rank
        
def find(subsets,node):
    
    if subsets[node].parent!=node:
        subsets[node].parent=find(subsets,subsets[node].parent)
        
    return subsets[node].parent

def union(subsets,x,y):
    xr=find(subsets,x)
    yr=find(subsets,y)
    if xr==yr:
        return False
    else:
        xr=subsets[xr]
        yr=subsets[yr]
        if xr.rank<yr.rank:
            xr.parent=yr.parent
        elif yr.rank<xr.rank:
            yr.parent=xr.parent
        else:
            xr.parent=yr.parent
            yr.rank+=1
        return True

def distance(p1,p2):
    x1,y1=p1
    x2,y2=p2
    return abs(x1-x2)+abs(y1-y2)

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        subsets={}
        for x,y in points:
            subsets[(x,y)]=Subsets((x,y),0)
        
        edges=[]
        
        for i in range(len(points)-1):
            p1=tuple(points[i])
            for j in range(i+1,len(points)):
                p2=tuple(points[j])
                edges.append((distance(p1,p2),p1,p2))
                
        edges.sort()
        ans=0
        
        for w,p1,p2 in edges:
            if union(subsets,p1,p2):
                ans+=w
                
        return ans
                
        
        
        
            

