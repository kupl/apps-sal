class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        occ = defaultdict(set)
        for row, col in reservedSeats:
            occ[row].add(col)

        ans = 0

        for row in occ:
            if all(i not in occ[row] for i in range(2, 10)):
                ans += 2
            elif all(i not in occ[row] for i in range(2, 6)):
                ans += 1
            elif all(i not in occ[row] for i in range(6, 10)):
                ans += 1
            elif all(i not in occ[row] for i in range(4, 8)):
                ans += 1

        return ans + 2 * (n - len(occ))
