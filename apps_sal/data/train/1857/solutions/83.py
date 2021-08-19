class Solution:

    def maxNumberOfFamilies(self, n: int, reserved: List[List[int]]) -> int:

        def getGroups(row):
            res = 0
            for group in [left, right]:
                if group.isdisjoint(d[row]):
                    res += 1
            if res >= 1:
                return res
            if middle.isdisjoint(d[row]):
                res += 1
            return res
        ans = 0
        d = defaultdict(set)
        (left, middle, right) = (set([2, 3, 4, 5]), set([4, 5, 6, 7]), set([6, 7, 8, 9]))
        for (row, col) in reserved:
            d[row].add(col)
        for row in d:
            ans += getGroups(row)
        m = len(d)
        return ans + (n - m) * 2
