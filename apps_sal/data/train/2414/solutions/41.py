class Solution:

    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        from itertools import combinations
        result = 0
        for x in combinations(arr, 3):
            if abs(x[0] - x[1]) <= a and abs(x[1] - x[2]) <= b and (abs(x[2] - x[0]) <= c):
                result += 1
        return result
