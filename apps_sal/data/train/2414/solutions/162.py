import itertools


class Solution:

    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        num = 0
        for triplet in itertools.combinations(arr, 3):
            if abs(triplet[0] - triplet[1]) <= a and abs(triplet[1] - triplet[2]) <= b and (abs(triplet[0] - triplet[2]) <= c):
                num += 1
        return num
