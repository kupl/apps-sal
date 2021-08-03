class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        ans = 0
        for i in range(len(arr) - 2):
            for j in range(i + 1, len(arr) - 1):
                for k in range(j + 1, len(arr)):
                    x = arr[i] - arr[j]
                    y = arr[j] - arr[k]
                    z = arr[i] - arr[k]
                    if abs(x) <= a and abs(y) <= b and abs(z) <= c:
                        ans += 1
        return ans
