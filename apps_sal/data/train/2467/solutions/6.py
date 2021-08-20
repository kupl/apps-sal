class Solution:

    def specialArray(self, nums: List[int]) -> int:
        for x in range(0, 1001):
            cnt = 0
            for e in nums:
                if e >= x:
                    cnt += 1
            if cnt == x:
                return x
        return -1
