import collections

class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        
        columns = {}
        for x,y in points:
            if x not in columns:
                columns[x] = []
            columns[x].append(y)
        
        lastx = {}
        ans = float('inf')
        
        for x in sorted(columns.keys()):
            column = columns[x]
            column.sort()
            for i,v in enumerate(column):
                for j in range(i):
                    val = column[j]
                    if (val, v) in lastx:
                        ans = min(ans, (x-lastx[val, v])*(v-val))
                    lastx[val, v] = x
                    
        return ans if ans < float('inf') else 0

