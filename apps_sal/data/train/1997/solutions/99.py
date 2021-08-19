class Solution:

    def removeCoveredIntervals(self, intervals):
        result = 0
        for i in range(len(intervals)):
            covered = False
            for j in range(len(intervals)):
                if i == j:
                    continue
                if self.covered(intervals[i], intervals[j]):
                    covered = True
                    break
            if not covered:
                result += 1
        return result

    def covered(self, i1, i2):
        c = i2[0]
        d = i2[1]
        a = i1[0]
        b = i1[1]
        return c <= a and b <= d
