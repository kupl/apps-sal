
class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))
        intervals = list(map(tuple, intervals))
        covered = set()
        for i, iv in enumerate(intervals):
            if iv in covered:
                continue
            for iv2 in intervals[i + 1:]:
                if iv2[0] > iv[1]:
                    break
                if iv[0] <= iv2[0] and iv[1] >= iv2[1]:
                    print(iv2)
                    covered.add(iv2)

        return len(intervals) - len(covered)
