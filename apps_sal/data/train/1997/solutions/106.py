class Solution:

    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        table = dict()
        for interval in intervals:
            if interval[0] not in intervals:
                table[interval[0]] = interval[1]
            elif interval[1] > table[interval[0]]:
                table[interval[0]] = interval[1]
        count = len(table) + 1
        keys = list(table.keys())
        cover = table[keys[0]]
        for key in table.keys():
            if table[key] <= cover:
                count -= 1
            else:
                cover = table[key]
        return count
