class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) < 2:
            return nums
        
        def merge(l1, l2):
            n1 = n2 = 0
            res = []
            
            while n1 < len(l1) and n2 < len(l2):
                if l1[n1] < l2[n2]:
                    res.append(l1[n1])
                    n1 += 1
                else:
                    res.append(l2[n2])
                    n2 += 1
                
            
            res += l1[n1:]
            res += l2[n2:]
            
            return res
        
        mid = len(nums) // 2
        
        return merge(self.sortArray(nums[:mid]), self.sortArray(nums[mid:]))
        
        

