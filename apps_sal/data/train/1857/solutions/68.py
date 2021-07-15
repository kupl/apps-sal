class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        seats = collections.defaultdict(int)
        for row, col in reservedSeats:
            seats[row] = seats[row] | (1 << (col - 1))

        res = 2 * n
        for reserved in seats.values():
            cnt = 0
            cnt += (reserved & int('0111100000', 2)) == 0
            cnt += (reserved & int('0000011110', 2)) == 0
            cnt += (reserved & int('0001111000', 2)) == 0 and cnt == 0
            res += (cnt - 2)
        return res
