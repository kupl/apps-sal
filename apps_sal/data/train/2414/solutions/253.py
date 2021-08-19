class Solution:

    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        n = len(arr)
        ans = 0
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                k = n - 1
                if abs(arr[i] - arr[j]) <= a:
                    while j < k:
                        if abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                            ans += 1
                        k -= 1
        return ans
