class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        BOTH, LEFT, RIGHT, MIDDLE = 0, 1, 2, 3
        required = [
            [2, 3, 4, 5, 6, 7, 8, 9], # BOTH
            [2, 3, 4, 5], # LEFT
            [6, 7, 8, 9], # RIGHT
            [4, 5, 6, 7] # MIDDLE
        ]
        fit = [2, 1, 1, 1]
        res = 0
        d = defaultdict(list)
        for i, j in reservedSeats:
            d[i].append(j)
        res = (n - len(d)) * 2 # 2 for each empty row
        for row in d.values():
            for k, needed in enumerate(required):
                if all(j not in row for j in needed):
                    res += fit[k]
                    break
        return res
