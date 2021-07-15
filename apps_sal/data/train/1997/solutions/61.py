class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        cover = [False for i in range(len(intervals))]
        for i in range(len(intervals)):
            for j in range(i+1, len(intervals)):
                a,b = intervals[i]
                c,d = intervals[j]
                if c <= a and b <= d:
                    cover[i] = True
                if a <= c and d <= b:
                    cover[j] = True
        ans = []
        print(cover)
        for i in range(len(cover)):
            if not cover[i]:
                ans.append(intervals[i])
        return len(ans)
