class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        q = []
        ans = 0
        L_n = len(nums)
        L_r = len(requests)
        for i in range(L_n):
            q.append(0)
        for i in range(L_r):
            q[requests[i][0]] += 1
            now = requests[i][1] + 1
            if now < len(q):
                q[now] -= 1
        for i in range(1, L_n):
            q[i] += q[i - 1]
        q.sort(reverse=True)
        nums.sort(reverse=True)
        for i in range(L_n):
            if q[i] == 0:
                q = q[0:i]
                break
        for i in range(len(q)):
            ans += q[i] * nums[i]
            ans = ans % (10**9 + 7)
        return ans
