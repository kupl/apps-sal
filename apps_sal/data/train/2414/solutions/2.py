import itertools


class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        triplets = 0
        for i, j, k in itertools.combinations(arr, 3):
            if abs(i - j) <= a and abs(j - k) <= b and abs(i - k) <= c:
                triplets += 1

        return triplets
