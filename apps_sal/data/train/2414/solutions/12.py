class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        count = 0
        for i, x in enumerate(arr):
            for j, y in enumerate(arr[i + 1:], i + 1):
                for k, z in enumerate(arr[j + 1:], j + 1):
                    if abs(x - y) <= a and abs(y - z) <= b and abs(x - z) <= c:
                        count += 1
        return count
