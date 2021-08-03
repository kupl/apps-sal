class Solution:
    def countOdds(self, low: int, high: int) -> int:

        # O(1) With Math
        odd_lowerbound, odd_upperbound = -1, -1

        # compute smallest odd number in range
        if low % 2 == 1:
            odd_lowerbound = low
        else:
            odd_lowerbound = low + 1

        # compute largest odd number in range
        if high % 2 == 1:
            odd_upperbound = high
        else:
            odd_upperbound = high - 1

        # compute the number of odd numbers in range
        return (odd_upperbound - odd_lowerbound) // 2 + 1
