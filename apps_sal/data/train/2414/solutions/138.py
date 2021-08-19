class Solution:

    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        count = 0
        for i in range(len(arr) - 2):
            for j in range(i + 1, len(arr)):
                for k in range(j + 1, len(arr)):
                    f = abs(arr[i] - arr[j]) <= a
                    s = abs(arr[j] - arr[k]) <= b
                    t = abs(arr[i] - arr[k]) <= c
                    count += f and s and t
        return count
