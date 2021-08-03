class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.merge(nums, 0, len(nums)-1)
        return nums
        
    def merge(self, nums, s, e):
        if s >= e:
            return
        
        m = (s+e) // 2
        i, j, k = s, m + 1, 0
        
        self.merge(nums, s, m)
        self.merge(nums, m+1, e)
        
        temp = [0 for _ in range(e-s+1)]
        
        while i<=m and j<=e:
            if nums[i] <= nums[j]:
                temp[k] = nums[i]
                i += 1
            else:
                temp[k] = nums[j]
                j += 1
            k += 1
        
        while i<=m:
            temp[k] = nums[i]
            i+=1
            k+=1
        
        while j<=e:
            temp[k] = nums[j]
            j+=1
            k+=1
        
        for i in range(len(temp)):
            nums[s+i] = temp[i]
            
\"\"\"
nums        : [4, 2, 3, 1]

            merge(0, 3)
            /   \\
        m(0,1)  m(2,3)
        /
    
         s
           e
         m
           i
             j
nums    [1,1]
             k
temp    [2,4]
    


\"\"\"
        
    
\"\"\"
if s + 1 <= e:
            m = (s+e) // 2
            i, j = s, m+1
            temp = [0 for _ in range(e-s+1)]
            k = 0
            while i <= m and j <= e:
                if nums[i] <= nums[j]:
                    temp[k] = nums[i]
                    i += 1
                else:
                    temp[k] = nums[k]
                    j += 1
                k += 1
            
            while i <= m:
                temp[k] = nums[i]
                k += 1
                i += 1
            
            for m in range(len(temp)):
                s[s+m] = temp[m]
        
\"\"\"
    


\"\"\"
10:51
0) Problem is 
    - sort an array
    - increasing order !!
    
    
    
1) Don't forget
- nums.length >= 1
- nums[i]  -50k ~ 50k

2) Brain Storming

                       s
                                e
                                
                          m
                       i
                             j
                       0  1  2  3
        nums        : [3, 2, 5, 4]
        
                      s   e
                      m
                      i  
                             j
        nums        : [3, 2]
        temp        : [2]
        
        if s + 1 <= e:
            m = (s+e) // 2
            i, j = s, m+1
            temp = [0 for _ in range(e-s+1)]
            k = 0
            while i <= m and j <= e:
                if nums[i] <= nums[j]:
                    temp[k] = nums[i]
                    i += 1
                else:
                    temp[k] = nums[k]
                    j += 1
                k += 1
            
            while i <= m:
                temp[k] = nums[i]
                k += 1
                i += 1
            
            for m in range(len(temp)):
                s[s+m] = temp[m]
        
        
            merge(s, e)
          /         \\
    merge(s, m)     merge(m+1, e)
    


\"\"\"
