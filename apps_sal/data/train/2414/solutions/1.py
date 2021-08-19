class Solution:

    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        res = (1 for (i, j, k) in combinations(arr, 3) if abs(i - j) <= a and abs(j - k) <= b and (abs(i - k) <= c))
        return sum(res)
