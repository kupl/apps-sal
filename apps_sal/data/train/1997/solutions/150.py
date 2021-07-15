
class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        start=len(intervals)
        temp=intervals.copy()
        for i, item in enumerate(intervals[:-1]):
            if item in temp:
                for item2 in intervals[i+1:]:
                    if item2 in temp:
                        if item2[0]>= item[0] and item2[1]<=item[1]:
                            start=start-1
                            temp.remove(item2)
                        elif item[0]>= item2[0] and item[1]<=item2[1]:
                            start=start-1
                            break
        return start
