from itertools import combinations


class Solution:

    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        num = len(arr)
        comb = combinations(arr, 3)
        counter = 0
        for m in comb:
            comb1 = list(m)
            i = comb1[0]
            j = comb1[1]
            k = comb1[2]
            if (abs(i - j) <= a) & (abs(j - k) <= b) & (abs(i - k) <= c):
                counter += 1
        return counter
