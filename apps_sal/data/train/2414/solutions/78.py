from itertools import combinations


class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:

        combs = combinations(arr, 3)

        counter = 0
        for i in list(combs):
            if abs(i[0] - i[1]) <= a and abs(i[1] - i[2]) <= b and abs(i[0] - i[2]) <= c:
                counter += 1

        return counter
