class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        def comparator(a, b):
            return a[0] - b[0]
        intervals.sort()
        removed = {}
        for index, interval in enumerate(intervals):
            for inner_index, inner_interval in enumerate(intervals):
                if index == inner_index:
                    continue
                    
                if index in removed or inner_index in removed:
                    continue
                    
                if inner_interval[0] >= interval[0] and inner_interval[1] <= interval[1]:
                    removed[inner_index] = True
                
        return len(intervals) - len(removed.keys())
