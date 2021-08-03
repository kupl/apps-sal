class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        length = len(intervals)
        if length <= 1:
            return length

        temp = intervals[:]

        i, j = 0, 1

        while i < len(intervals) - 1:
            j = i + 1
            while j < len(intervals):
                if self.ainbHelper(intervals[i], intervals[j]) == True:
                    try:
                        temp.remove(intervals[i])
                    except:
                        pass
                    break
                elif self.ainbHelper(intervals[j], intervals[i]) == True:
                    try:
                        temp.remove(intervals[j])
                    except:
                        pass
                    j += 1
                else:
                    j += 1
            i += 1

        return len(temp)

    def ainbHelper(self, a: List[int], b: List[int]) -> bool:
        if a[0] < b[0]:
            return False
        if a[1] > b[1]:
            return False
        else:
            return True
