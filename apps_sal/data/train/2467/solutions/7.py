class Solution:

    def specialArray(self, nums: List[int]) -> int:
        for x in range(-5, 1002):
            cnt = 0
            for y in nums:
                if y >= x:
                    cnt += 1
            if cnt == x:
                return x
        return -1
