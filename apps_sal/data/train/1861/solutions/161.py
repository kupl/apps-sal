class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        dx = defaultdict(list)
        for x, y in points:
            dx[x].append(y)
        lastx = defaultdict(list)
        ans = float('inf')
        
        for x in sorted(dx):
            col = dx[x]
            col.sort()
            for i in range(len(col)-1):
                for j in range(i+1, len(col)):
                    y1 = col[i]
                    y2 = col[j]
                    if (y1,y2) in lastx:
                        for xs in lastx[y1,y2]:
                            ans = min(ans, (abs(y2-y1))*(abs(x-xs)))
                    lastx[y1,y2].append(x)
        return ans if ans<float('inf') else 0
            
            
        

