class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        count = 0
        for i in range(0, len(arr) - 2):
            for j in range(i + 1, len(arr) - 1):
                for k in range(j + 1, len(arr)):
                    check1 = abs(arr[i] - arr[j]) <= a
                    check2 = abs(arr[j] - arr[k]) <= b
                    check3 = abs(arr[i] - arr[k]) <= c
                    count += 1 if (check1 and check2 and check3) else 0
        return count
