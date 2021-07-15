class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums)<=1:
            return nums
        
        sorted_list = nums
        
        while len(sorted_list)>1:
            
            x = sorted_list.pop(0)
            y = sorted_list.pop(0)
            sorted_list.append(self.merge(x,y))
            
            
            
        
        return sorted_list[0]
            
            
        
        
        
    def merge(self,list1, list2):
        
        if isinstance(list1, int):
            list1 = [list1]
        if isinstance(list2, int):
            list2 = [list2]
        ret = []
            
        list1_cursor = list2_cursor = 0
        
        while list1_cursor < len(list1) and list2_cursor < len(list2):
            if list1[list1_cursor] < list2[list2_cursor]:
                ret.append(list1[list1_cursor])
                list1_cursor += 1
                
            else:
                ret.append(list2[list2_cursor])
                list2_cursor += 1
                    
            
        ret.extend(list1[list1_cursor:])
        ret.extend(list2[list2_cursor:])
        
        return ret
