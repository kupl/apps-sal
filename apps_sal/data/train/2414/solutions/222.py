class Solution:

    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        count = 0
        for (i, x) in enumerate(arr):
            for (j, y) in enumerate(arr[i + 1:]):
                if abs(x - y) <= a:
                    for z in arr[j + i + 2:]:
                        count += abs(y - z) <= b and abs(x - z) <= c
        return count
