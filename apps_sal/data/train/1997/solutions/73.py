class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        exclude = list()
        for ind, left in enumerate(intervals[:-1]):
            if left in exclude:
                continue
            for right in intervals[ind+1:]:
                if right in exclude:
                    continue
                elif (right[0] <= left[0] and left[1] <= right[1]):
                    exclude.append(left)
                    break
                elif(left[0] <= right[0] and right[1] <= left[1]):
                    exclude.append(right)
                else:
                    continue

                    
        return len(intervals) - len(exclude)

