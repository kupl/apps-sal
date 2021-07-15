class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        track = 0
        for num in nums:
            count = 0
            if len(str(num)) % 2 ==0:
                track += 1
        return track
