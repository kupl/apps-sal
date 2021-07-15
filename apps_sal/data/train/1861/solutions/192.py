class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        mx = defaultdict(set)
        for x, y in points: mx[x].add(y)
        ans, n = float('inf'), len(points)
        for i in range(n-1):
            x1, y1 = points[i]
            for j in range(i+1, n):                
                x2, y2 = points[j]
                if x2 == x1 or y2 == y1 or y2 not in mx[x1] or y1 not in mx[x2]: continue                    
                ans = min(abs(x2-x1)*abs(y2-y1), ans)
        return 0 if ans == float('inf') else ans
