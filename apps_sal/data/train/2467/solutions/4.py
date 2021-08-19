class Solution:

    def specialArray(self, nums: List[int]) -> int:
        n = len(nums)
        temp = [0 for i in range(n)]
        if nums == temp:
            return -1
        for x in range(1001):
            cnt = 0
            for i in nums:
                if i >= x:
                    cnt += 1
            if cnt == x:
                return x
        return -1
