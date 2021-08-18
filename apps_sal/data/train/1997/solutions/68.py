class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:

        intervals = sorted(intervals, key=lambda x: (x[0], - x[1]))
        if len(intervals) == 1:
            return 1

        remove_indices = []

        for p1, (l1, r1) in enumerate(intervals[:-1]):

            for p2, (l2, r2) in enumerate(intervals[p1 + 1:]):

                if l1 <= l2 and r1 >= r2:
                    remove_indices.append(p2 + p1)
                elif l1 < l2 < r1:
                    continue
                else:
                    break

        return len([interval for idx, interval in enumerate(intervals) if idx not in remove_indices])
