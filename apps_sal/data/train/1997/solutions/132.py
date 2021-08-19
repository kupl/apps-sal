class Solution:

    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        answers = []
        for i in intervals:
            cints = intervals.copy()
            cints.remove(i)
            if all(map(lambda j: i[0] < j[0] or i[1] > j[1], cints)):
                answers.append(i)
        return len(answers)
