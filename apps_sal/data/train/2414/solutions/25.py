from typing import List


class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        total_good_triplets = 0
        for i in range(len(arr) - 2):
            for j in range(i + 1, len(arr) - 1):
                for k in range(j + 1, len(arr)):
                    if abs(arr[i] - arr[j]) <= a and abs(
                        arr[k] - arr[j]) <= b and abs(
                            arr[i] - arr[k]) <= c:
                        total_good_triplets += 1
        return total_good_triplets
