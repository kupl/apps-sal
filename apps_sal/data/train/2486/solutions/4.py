class Solution:
    def numberOfSteps (self, num: int) -> int:
        count=0
        while num>0:
            if num&1:
                count+=1
            num=num>>1
            count+=1
            
        return count-1 if count > 0 else count
