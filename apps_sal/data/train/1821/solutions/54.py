class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        if len(nums) == 1:
            return nums
        
        n = int(len(nums) / 2)
        a1 = nums[:(n)]
        a2 = nums[(n):]
        
        a1 = self.sortArray(a1)
        a2 = self.sortArray(a2)
        
        return self.merge(a1,a2)
    
    def merge(self,a1,a2):
        i1 = 0
        i2 = 0
        ret = []
        
        while i1 < len(a1) and i2 < len(a2):
            if a1[i1] < a2[i2]:
                ret.append(a1[i1])
                i1 += 1
            else:
                ret.append(a2[i2])
                i2 += 1
        
        while i1 < len(a1):
            ret.append(a1[i1])
            print((a1[i1]))
            i1 += 1
        while i2 < len(a2):
            ret.append(a2[i2])
            print((a2[i2]))
            i2 += 1
        return ret
                
                

