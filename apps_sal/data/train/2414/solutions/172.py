class Solution:

    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        count = 0
        for i in range(len(arr) - 2):
            for j in range(i + 1, len(arr) - 1):
                for k in range(j + 1, len(arr)):
                    goodA = abs(arr[i] - arr[j]) <= a
                    goodB = abs(arr[j] - arr[k]) <= b
                    goodC = abs(arr[i] - arr[k]) <= c
                    if all((goodA, goodB, goodC)):
                        count += 1
        return count
