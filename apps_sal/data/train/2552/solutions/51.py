class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        b = {}
        for a in arr:
            if a not in b:
                b[a] = 1
            else:
                b[a] += 1
        c = [[k, v] for k, v in sorted(b.items(), key=lambda item: item[1])]
        return c[-1][0]
