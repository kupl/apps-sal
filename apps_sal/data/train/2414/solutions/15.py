class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        count = 0
        for i, item in enumerate(arr):
            for j in range(i + 1, len(arr)):
                for k in range(j + 1, len(arr)):
                    if abs(item - arr[j]) <= a and abs(arr[j] - arr[k]) <= b and abs(item - arr[k]) <= c:
                        count += 1
        return count
