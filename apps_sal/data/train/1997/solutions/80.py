class Solution:

    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        arr = []
        for val in intervals:
            for interval in intervals:
                if interval[0] == val[0] and interval[1] == val[1]:
                    continue
                if interval[0] <= val[0] and interval[1] >= val[1]:
                    break
            else:
                arr.append(val)
        return len(arr)
