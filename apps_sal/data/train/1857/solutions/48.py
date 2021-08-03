class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:

        g = defaultdict(int)
        for r, s in reservedSeats:
            g[r] |= {0: 0, 1: 4, 2: 5, 3: 3, 4: 2, 5: 0}[s >> 1]
        return sum(2 if s == 0 else 1 if s < 7 else 0 for r, s in g.items()) + (n - len(g)) * 2
