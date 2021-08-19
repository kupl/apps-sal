class Solution:

    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        i = set(map(tuple, intervals))
        l = set()
        for a in i:
            for b in i - {a} - l:
                if a == b:
                    continue
                if covered(a, b):
                    l.add(a)
                    break
        return len(i) - len(l)


def covered(a, b):
    return b[0] <= a[0] and a[1] <= b[1]
