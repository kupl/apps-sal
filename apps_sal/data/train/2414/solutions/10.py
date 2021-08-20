class Solution:

    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        s = 0
        for (i, m) in enumerate(arr):
            for (j, n) in enumerate(arr[i + 1:]):
                for (k, q) in enumerate(arr[i + j + 2:]):
                    if abs(m - n) <= a and abs(n - q) <= b and (abs(m - q) <= c):
                        s += 1
        return s
