class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        n_good = 0
        for n, i in enumerate(arr):
            for o, j in enumerate(arr[n+1:]):
                for k in arr[n+o+2:]:
                    if abs(i-j) <= a and abs(j-k) <= b and abs(i-k) <= c:
                        n_good = n_good+1
        return n_good
