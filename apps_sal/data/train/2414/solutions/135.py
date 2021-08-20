class Solution:

    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        cnt = 0
        for (in_i, i) in enumerate(arr):
            for (in_j, j) in enumerate(arr):
                if in_i < in_j:
                    for (in_k, k) in enumerate(arr):
                        if in_i < in_j < in_k:
                            if abs(i - j) <= a and abs(j - k) <= b and (abs(i - k) <= c):
                                cnt += 1
        return cnt
