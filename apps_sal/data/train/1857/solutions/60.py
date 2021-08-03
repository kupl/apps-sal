class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        res = 0
        seats = collections.defaultdict(int)
        for r, seat in reservedSeats:
            seats[r] |= (1 << (seat - 1))
        for reserved in list(seats.values()):
            curr = 0
            if (reserved & int('0111100000', 2)) == 0:
                curr += 1
            if (reserved & int('0000011110', 2)) == 0:
                curr += 1
            if (reserved & int('0001111000', 2)) == 0 and curr == 0:
                curr += 1
            res += curr
        return res + 2 * (n - len(seats))
