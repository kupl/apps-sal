class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        nums = [0] * 1001
        ans = 0
        length = len(arr)
        for j in range(length):
            for k in range(j + 1, length):
                if abs(arr[j] - arr[k]) <= b:
                    r = min(arr[j] + a, arr[k] + c, 1000)
                    l = max(arr[j] - a, arr[k] - c, 0)
                    if r >= l:
                        ans += nums[r] if l == 0 else nums[r] - nums[l - 1]
            for m in range(arr[j], 1001):
                nums[m] += 1
        return ans
