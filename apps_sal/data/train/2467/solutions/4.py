class Solution:
    def specialArray(self, nums: List[int]) -> int:
        # n --> length of given array
        n = len(nums)

        # temporary array with all elements 0
        temp = [0 for i in range(n)]

        # if all elements are 0 then given array is not special
        if nums == temp:
            return -1

        # check for each number from 0 to 1000 that for ith number there are exactly i numbers greater than or equal to i.
        for x in range(1001):
            cnt = 0
            for i in nums:
                if i >= x:
                    cnt += 1
            if cnt == x:
                return x
        return -1
