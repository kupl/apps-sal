class Solution:

    def countOdds(self, low: int, high: int) -> int:
        (odd_lowerbound, odd_upperbound) = (-1, -1)
        if low % 2 == 1:
            odd_lowerbound = low
        else:
            odd_lowerbound = low + 1
        if high % 2 == 1:
            odd_upperbound = high
        else:
            odd_upperbound = high - 1
        return (odd_upperbound - odd_lowerbound) // 2 + 1
