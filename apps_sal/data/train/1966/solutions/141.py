class Solution:
  #  def helper(self, l):
  #      num = 0
  #      ct = 0
  #      for j in range(len(l)):
  #          if l[j] == 1:
  #              ct += 1
  #          else:
  #              ct = 0
  #          num += ct
  #      
  #      return num
  #  
  #
  #  def numSubmat(self, mat: List[List[int]]) -> int:
  #      m = len(mat)
  #      n = len(mat[0])
  #      tot_sum = 0
  #      for i1 in range(m):
  #          l = [1]*n
  #          for i2 in range(i1, m):
  #              for j in range(n):
  #                  l[j] &= mat[i2][j]
  #              tot_sum += self.helper(l)
  #              
  #      return tot_sum
  #  
    
    def helper(self, arr):
        tracker = [0] * len(arr)
        stack = []
        
        for i in range(len(arr)):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            if stack:
                tracker[i] = tracker[stack[-1]]
                tracker[i] += arr[i] * (i - stack[-1])
            else:
                tracker[i] = arr[i] * (i + 1)
            stack.append(i)
        
        return sum(tracker)
    
    def numSubmat(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        column_track = [0] * n
        res = 0
        
        for i in range(m):
            for j in range(n):
                column_track[j] = 0 if mat[i][j] == 0 else column_track[j] + 1
            res += self.helper(column_track)
        
        return res
            
    
        
            

