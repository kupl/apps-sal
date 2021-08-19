class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        reserved = dict()
        for r in reservedSeats:
            reserved[r[0]] = reserved.get(r[0], set())
            reserved[r[0]].add(r[1])

        # we can fit 2 groups for all rows with no reservations
        ans = 2 * (n - len(reserved.keys()))
        for _, reservations in reserved.items():
            middle = True
            if all([seat not in reservations for seat in [2, 3, 4, 5]]):
                ans += 1
                middle = False
            if all([seat not in reservations for seat in [6, 7, 8, 9]]):
                ans += 1
                middle = False
            if middle and all([seat not in reservations for seat in [4, 5, 6, 7]]):
                ans += 1

        return ans
