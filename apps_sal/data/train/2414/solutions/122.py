class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        if not arr:
            return 0

        result = 0
        for i in range(len(arr) - 2):
            for j in range(i + 1, len(arr) - 1):
                for k in range(j + 1, len(arr)):
                    first = abs(arr[i] - arr[j]) <= a
                    second = abs(arr[j] - arr[k]) <= b
                    third = abs(arr[i] - arr[k]) <= c
                    if first and second and third:
                        result += 1
        return result
