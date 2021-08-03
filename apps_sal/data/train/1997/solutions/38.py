class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        covered = set()
        for i in range(len(intervals) - 1):
            a1, b1 = intervals[i]
            for j in range(i + 1, len(intervals)):
                a2, b2 = intervals[j]
                # print('Interals: [{},{}) vs [{},{})'.format(
                #     a1, b1, a2, b2))
                if a2 <= a1 and b1 <= b2:
                    #print('covered: {} by {}'.format(i, j))
                    covered.add(i)
                elif a1 <= a2 and b2 <= b1:
                    #print('covered: {} by {}'.format(j, i))
                    covered.add(j)
        return len(intervals) - len(covered)
