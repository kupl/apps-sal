class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        
        new_arr = []
        
        l = len(arr)
        
        last = arr[-1]
        
        map_num = {}
        
        for i in range(l):
            
            map_num[arr[i]] = 1
        
        for i in range(1,last+2):
            if i not in map_num:
                new_arr.append(i)
                
        print(new_arr)
                
        if len(new_arr) == 0:
            return last+k
        
        elif k > len(new_arr):
            return new_arr[-1] + k - len(new_arr) 
        
        else:
            return new_arr[k-1]
        
        
                
            

