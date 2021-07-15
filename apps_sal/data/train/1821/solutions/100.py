class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <=1:
            return nums
        mid = len(nums)//2
        l_list = self.sortArray(nums[:mid])
        r_list = self.sortArray(nums[mid:])
        return self.merge(l_list,r_list)
    
    def merge(self,a,b):
        
        a_l = b_l = 0
        m = []
        while a_l < len(a) and b_l < len(b):
            if a[a_l] < b[b_l]:
                m.append(a[a_l])
                a_l += 1
            else:
                m.append(b[b_l])
                b_l += 1
            
        
            
        m.extend(a[a_l:])
        m.extend(b[b_l:])
        
        return m
            
        

