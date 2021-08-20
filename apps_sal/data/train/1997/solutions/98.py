class Solution:

    def compare(self, intervalA: List[int], intervalB: List[int]) -> int:
        if intervalA[0] <= intervalB[0] and intervalA[1] >= intervalB[1]:
            return 1
        if intervalB[0] <= intervalA[0] and intervalB[1] >= intervalA[1]:
            return -1
        return 0

    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        result = len(intervals)
        index = 0
        while index < len(intervals):
            itemA = intervals[index]
            removes = []
            for i in range(index + 1, len(intervals)):
                itemB = intervals[i]
                comp = self.compare(itemA, itemB)
                if comp == 0:
                    continue
                if comp == 1:
                    removes.append(i)
                elif comp == -1 and index not in removes:
                    removes.append(index)
            if len(removes) == 0:
                index += 1
            else:
                removes.sort()
                removes.reverse()
                for k in range(len(removes)):
                    intervals.remove(intervals[removes[k]])
                if index not in removes:
                    index += 1
            result -= len(removes)
        return result
