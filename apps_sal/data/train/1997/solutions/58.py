class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        count = [0] * len(intervals)
        for i in range(len(intervals) - 1):
            a = intervals[i][0]
            b = intervals[i][1]
            for j in range(i + 1, len(intervals)):
                x = intervals[j][0]
                y = intervals[j][1]
                if x <= a and b <= y:
                    # print(\"first\")
                    # print(x,y ,\"takes \",a,b)
                    count[i] = 1
                    # count[j] = 1
                elif a <= x and y <= b:
                    # print(a,b ,\"takes \",x,y)
                    # print(\"Second\")
                    # count[i] = 1
                    count[j] = 1
        ans = 0
        for c in count:
            if c == 0:
                ans += 1
        return ans
