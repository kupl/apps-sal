from collections import defaultdict
class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        n=len(intervals)
        m=n
        visited=defaultdict(lambda:False)
        for i in range(n):
            for j in range(n):
                if i==j or visited[j]:
                    continue
                if intervals[i][0]<=intervals[j][0]:
                    if intervals[i][1]>=intervals[j][1]:
                        visited[j]=True
                        m-=1
        return m
