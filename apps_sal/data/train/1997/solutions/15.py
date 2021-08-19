class Solution:

    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        new = sorted(intervals, key=lambda x: x[1] - x[0], reverse=True)
        ans = []
        for (i, v) in enumerate(new):
            flag = False
            for elem in new[:i]:
                if v[0] >= elem[0] and v[1] <= elem[1]:
                    flag = True
            if flag == False:
                ans.append(v)
        return len(ans)
