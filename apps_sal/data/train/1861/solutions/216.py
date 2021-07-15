class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        def intersection(lst1, lst2): 
            return list(set(lst1) & set(lst2)) 
  
        col=defaultdict(list)
#        row=defaultdict(list)
        ans=float('inf')
        for point in points:
            col[point[0]].append(point[1])
#            row[point[1]].append(point[0])
        cols=list(col.keys())
        for i1 in range(len(cols)):
            for i2 in range(i1+1,len(cols)):
                col1=cols[i1]
                col2=cols[i2]
                il=sorted(intersection(col[col1],col[col2]))
                for i in range(1,len(il)):
                    ans=min(ans,(il[i]-il[i-1])*abs(col2-col1))
        return ans if ans<float('inf') else 0
