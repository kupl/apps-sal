class NumArray:
     def __init__(self, nums):
         """
         :type nums: List[int]
         """
         self.nums = nums
         self.step = 20
         self.cache = [0] * math.ceil(len(nums)/self.step)
         for i in range(len(nums)):
             self.cache[i//self.step] += nums[i]
 
     def update(self, i, val):
         """
         :type i: int
         :type val: int
         :rtype: void
         """
         old = self.nums[i]
         self.nums[i] = val
         self.cache[i//self.step] += (val - old)
         
     def sumRange(self, i, j):
         """
         :type i: int
         :type j: int
         :rtype: int
         """
         if (j//self.step - i//self.step) > 1:     
             spliti = ((i//self.step) + 1) * self.step - 1
             
             splitj = ((j//self.step)) * self.step
             
             sumi = sum(self.nums[i:(spliti+1)])
             sumj = sum(self.nums[splitj:(j+1)])
             sumbetween = sum(self.cache[((i//self.step) +1):((j//self.step))])
             return sumi + sumj + sumbetween
         else:
             return sum(self.nums[i:(j+1)])
 
         
 
 
 # Your NumArray object will be instantiated and called as such:
 # obj = NumArray(nums)
 # obj.update(i,val)
 # param_2 = obj.sumRange(i,j)

