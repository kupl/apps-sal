from itertools import combinations


class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        count = 0

        combs = combinations(arr, 3)
        return sum((abs(comb[0] - comb[1]) <= a and abs(comb[1] - comb[2]) <= b and abs(comb[0] - comb[2]) <= c) for comb in combs)
