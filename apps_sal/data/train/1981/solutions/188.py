class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        diff = [0 for i in range(len(nums) + 1)]

        for r in requests:
            diff[r[0]] += 1
            diff[r[1] + 1] -= 1
        for i in range(1, len(diff)):
            diff[i] = diff[i - 1] + diff[i]
        print(diff)
        diff.sort(reverse=True)
        nums.sort(reverse=True)
        answer = 0

        i = 0
        while diff[i] != 0:
            answer += diff[i] * nums[i]
            answer = answer % (1e9 + 7)
            i += 1
        return int(answer)
