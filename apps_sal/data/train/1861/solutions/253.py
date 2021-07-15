\"\"\"
总体思路是，enum所有点pair，把他们单做diagnal上的两个点，这样我们只要在points中找有没有另外两个点就好了。
注意这里我们直接把拿出来的点当做左上和右下，为什么可以这么做？因为我们要穷举所有的点pair，所以肯定能找到一个这样的点pair
\"\"\"
class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        hashset = set()
        # for lookup
        for p in points:
            hashset.add((p[0], p[1]))
        
        ans = sys.maxsize
        # we enumerate all diagnal points
        for i in range(len(points)-1):
            for j in range(i+1, len(points)):
                x1, y1 = points[i]
                x2, y2 = points[j]
                if x1 == x2 or y1 == y2: # we need diagnal points
                    continue
                if (x1, y2) in hashset and (x2, y1) in hashset:
                    ans = min(ans, abs((x2 - x1) * (y1 - y2)))
        return 0 if ans == sys.maxsize else ans            
                
                
        
