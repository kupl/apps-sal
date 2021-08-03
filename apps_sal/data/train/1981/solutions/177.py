class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        mex = 10**5
        mex += 5
        ans = [0 for i in range(mex)]
        for i in requests:
            x, y = i
            ans[x] += 1
            ans[y + 1] -= 1
        for i in range(1, mex):
            ans[i] = ans[i] + ans[i - 1]
        nums.sort(reverse=True)
        freq = []
        for i in ans:
            if i != 0:
                freq.append(i)
        freq.sort(reverse=True)
        mod = 10**9
        mod += 7
        cnt = 0
        for i in range(min(len(freq), len(nums))):
            cnt = (cnt + ((freq[i] * nums[i]) % mod)) % mod
        return cnt
