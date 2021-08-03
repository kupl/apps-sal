class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        print(nums)
        if nums == []:
            return []
        p = nums.pop()
        s = []
        b = []
        for i in nums:
            if i > p:
                b.append(i)
            else:
                s.append(i)
        return self.sortArray(s.copy()) + [p] + self.sortArray(b.copy())
