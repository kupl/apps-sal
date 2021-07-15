class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        ans=float('inf')
        s=set()
        for i,j in points:
            for x,y in s:
                if (i,y) in s and (x,j) in s:
                    ans=min(ans,abs(i-x)*abs(j-y))
            s.add((i,j))
        return ans if ans!=float('inf') else 0

