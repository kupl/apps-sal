class NumArray:
 
     def __init__(self, nums):
         """
         :type nums: List[int]
         """
         l = len(nums)
         self.nums = nums
         self.bit = [0] * (l+1)
         for i in range(1, l+1):
             self.update_delta(i, nums[i-1])
 
     def update(self, i, val):
         """
         :type i: int
         :type val: int
         :rtype: void
         """
         bit = self.bit
         delta = val - self.nums[i]
         self.nums[i] = val
         self.update_delta(i+1, delta)
 
     def sumRange(self, i, j):
         """
         :type i: int
         :type j: int
         :rtype: int
         """
         return self.get_sum(j+1) - self.get_sum(i)
     
     def get_sum(self, i):
         bit = self.bit
         res = 0
         while i > 0:
             res += bit[i]
             i -= (i & -i)
         
         return res
     
     def update_delta(self, i, delta):
         bit = self.bit
         l = len(bit)
         while i < l:
             bit[i] += delta
             i += (i & -i)
             
         
 
 
 # Your NumArray object will be instantiated and called as such:
 # obj = NumArray(nums)
 # obj.update(i,val)
 # param_2 = obj.sumRange(i,j)

