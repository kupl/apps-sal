class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        nums = list(set(arr))
        for i in nums:
            if(arr.count(i) >= (len(arr) // 4) + 1):
                return i
        return False
