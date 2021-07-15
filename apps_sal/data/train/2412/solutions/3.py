class Solution:
    def removeDuplicates(self, S: str) -> str:
        str_2_arr = list(S)
        while True:
            tmp_arr = []
            i = 0
            while i < len(str_2_arr):
                if i < len(str_2_arr)-1 and str_2_arr[i] == str_2_arr[i+1]:
                    i += 2
                    continue
                    
                tmp_arr.append(str_2_arr[i])
                i += 1
  
            if str(tmp_arr) == str(str_2_arr):
                break
              
            str_2_arr =  list(tmp_arr)  
            tmp_arr = []
            
        return ''.join(str_2_arr)
            
            
            

