from collections import defaultdict
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        
        
        count = 0
        
        thresh_count = int(.25*len(arr))
        dic = defaultdict(int)
        
        for ele in arr:
            dic[ele]+=1
            if dic[ele]> thresh_count:
                return ele
            
        
        

