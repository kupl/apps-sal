class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        n = len(arr)
        count = 0
        for i in range(n):
            for j in range(i, n):
                for k in range(j, n):
                    if i != j != k and j != k:
                        if (abs(arr[i] - arr[j]) <= a
                           and abs(arr[j] - arr[k]) <= b
                           and abs(arr[i] - arr[k]) <= c):
                            count += 1
        return count
