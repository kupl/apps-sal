class Solution:
    
    def checkIntvl(self, a: List[int], b: List[int]) -> bool:
        return b[0] <= a[0] and b[1] >= a[1]

    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        count = 0
        for i, i1 in enumerate(intervals):
            is_covered = False
            for j, i2 in enumerate(intervals):
                if i == j:
                    continue
                else:
                    is_covered = self.checkIntvl(i1, i2)
                    if is_covered:
                        break
            if not is_covered:
                count += 1
        return count
