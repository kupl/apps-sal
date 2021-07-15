class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        flag = [True for i in range(n)]
        ctr = n
        for i in range(n):
            for j in range(n):
                if i!=j and flag[i] and flag[j]:
                    a,b = intervals[i]
                    c,d = intervals[j]
                    if(c<=a and b<=d):
                        flag[i] = False
                        ctr-=1
                    elif(a<=c and d<=b):
                        flag[j] = False
                        ctr-=1
        return ctr
