class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        sorted_intervals = sorted(intervals, key=lambda x: (x[0], -x[1]))
        covered = [False for interval in intervals]
        print(sorted_intervals)

        for outer_index, outer in enumerate(sorted_intervals):
            for inner_index, inner in enumerate(sorted_intervals[outer_index + 1:]):
                if outer[0] <= inner[0] and outer[1] >= inner[1]:
                    covered[inner_index + outer_index + 1] = True

        print(covered)

        return sum((not cover for cover in covered))
