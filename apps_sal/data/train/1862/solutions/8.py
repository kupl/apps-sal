class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        
        last = len(arr)
        ans = []
        
        while last > 1:
            #print(f\"last={last} ans={ans} arr={arr}\")
            max_pos = 0
            max_v = -float('inf')
            for i in range(last):
                if arr[i] > max_v:
                    max_v = arr[i]
                    max_pos = i
                    
        
                
            ans.append(max_pos+1)
            ans.append(last)
            arr[:max_pos+1] = arr[:max_pos+1][::-1]
            arr[:last] = arr[:last][::-1]
                
            last -= 1
        return ans
    
    

