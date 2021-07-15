from itertools import combinations

class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        count = 0
        for (A, B, C) in combinations(arr, 3):
            if abs(A - B) <= a and abs(B - C) <= b and abs(C - A) <= c:
                count += 1
        return count
