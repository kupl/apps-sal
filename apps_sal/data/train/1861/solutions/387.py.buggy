\"\"\"
sol1 hashmap 存 x:[y1,y2,...], 寻找对角线diagonal上的两点，再检查是否存在剩下的两点
timeO(n^2) spaceO(n^2)
\"\"\"
class Solution:
    \"\"\"sol1 diagonal+hashmap timeO(n^2) spaceO(n^2)\"\"\"
    def minAreaRect(self, points: List[List[int]]) -> int:
        x2y = collections.defaultdict(set)
        minArea = float('inf')
        
        for x,y in points: # hashmap <x, {y1,y2,...}>
            x2y[x].add(y)
        
        # find diagnal (x1,y1) -> (x2,y2)
        for x1,y1 in points:
            for x2,y2 in points:
                if x1==x2 or y1==y2: continue # in the same row/column, cannot form retangle
                elif y2 in x2y[x1] and y1 in x2y[x2]:
                    minArea = min(minArea, abs((x1-x2)*(y1-y2)) )
                
        if minArea<float('inf'): return minArea
        return 0
