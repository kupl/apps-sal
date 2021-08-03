class Solution:
    def countGoodTriplets(self, arr, a, b, c):
        return sum(abs(n - arr[j]) <= a and abs(arr[j] - arr[k]) <= b and abs(n - arr[k]) <= c for i, n in enumerate(arr) for j in range(i + 1, len(arr) - 1) for k in range(j + 1, len(arr)))
