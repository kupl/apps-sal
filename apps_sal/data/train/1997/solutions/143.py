class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        dictionary = {}
        intervals.sort(key=lambda x: (x[1]))
        j = 0

        while j != len(intervals):
            idx = j + 1
            minima = intervals[j][0]
            while idx < len(intervals):
                if intervals[idx][1] == intervals[j][1]:
                    minima = min(minima, intervals[idx][0])
                    intervals.pop(idx)
                    idx += 1
                else:
                    break
            intervals[j][0] = minima
            value = intervals[j][0]
            if value not in dictionary:
                dictionary[value] = 1
            else:
                dictionary[value] += 1
            j += 1
        counter = len(intervals)
        for value in intervals:
            for elem in dictionary:
                if elem == value[0] and dictionary[elem] > 1:
                    counter -= 1
                    break
                if elem < value[0] and dictionary[elem] > 0:
                    counter -= 1
                    break
            dictionary[value[0]] -= 1
        return counter
