class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        total = len(intervals)
        for i, inner in enumerate(intervals):
            for o, outer in enumerate(intervals):
                if outer[0] <= inner[0] and outer[1] >= inner[1] and i != o:
                    #print(f\"inner {inner} outer {outer}\")
                    total -= 1
                    break
        return total
