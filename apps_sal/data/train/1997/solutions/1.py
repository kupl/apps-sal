class Solution:
    def removeCoveredIntervals(self, l: List[List[int]]) -> int:
        l.sort(reverse=True,key=lambda x:(x[1],-x[0]))
        n=len(l)
        c=n
        for i in range(n-1):
            if(l[i][0]<=l[i+1][0] and l[i][1]>=l[i+1][1]):
                l[i+1]=l[i]
                c-=1
        return c
