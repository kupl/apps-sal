class Solution:

    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        count = 0
        for (i, arr_i) in enumerate(arr):
            for (j, arr_j) in enumerate(arr[i + 1:]):
                for arr_k in arr[i + j + 2:]:
                    if abs(arr_i - arr_j) <= a and abs(arr_j - arr_k) <= b and (abs(arr_i - arr_k) <= c):
                        count += 1
        return count
