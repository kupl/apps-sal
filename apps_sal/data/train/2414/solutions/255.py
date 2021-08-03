class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        ans = 0
        LEN = len(arr)
        for i in range(LEN - 2):
            for j in range(i + 1, LEN - 1):
                if abs(arr[i] - arr[j]) > a:
                    continue
                for k in range(j + 1, LEN):
                    if (abs(arr[j] - arr[k]) > b) | (abs(arr[i] - arr[k]) > c):
                        continue
                    ans += 1
        return ans
