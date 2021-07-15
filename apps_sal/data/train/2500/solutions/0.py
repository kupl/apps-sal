class Solution:
    def maxPower(self, s: str) -> int:
        n = len(s) 
        count = 0
        res = s[0] 
        cur_count = 1
  
        # Traverse string except  
        # last character 
        for i in range(n): 
          
            # If current character  
            # matches with next 
            if (i < n - 1 and 
                s[i] == s[i + 1]): 
                cur_count += 1
  
            # If doesn't match, update result 
            # (if required) and reset count 
            else: 
                if cur_count > count: 
                    count = cur_count 
                    res = s[i] 
                cur_count = 1
        return count 
       
        
        

