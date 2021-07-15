class Solution:
    
    def minStartValue(self, nums: List[int]) -> int:
        start =1
        s=1
        for n in nums:
            s+=n
            if s<1:
                start+=1-s
                s=1
        return start
