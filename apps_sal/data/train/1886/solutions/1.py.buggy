from math import sqrt
 class NumArray(object):
 
     def __init__(self, nums):
         """
         :type nums: List[int]
         """
         if nums:
             k=int(sqrt(len(nums)))
             add,i=[],0
             while i<=len(nums)-k:
                 add.append(sum(nums[i:i+k]))
                 i+=k
             if i!=len(nums):
                 add.append(sum(nums[i:]))
             self.nums,self.add,self.k=nums,add,k
         
 
     def update(self, i, val):
         """
         :type i: int
         :type val: int
         :rtype: void
         """
         self.add[i//self.k]+=val-self.nums[i]
         self.nums[i]=val
         
         
 
     def sumRange(self, i, j):
         """
         :type i: int
         :type j: int
         :rtype: int
         """
         def func(i):
             return sum(self.add[:i//self.k])+sum(self.nums[(i//self.k)*self.k:i+1]) if i>=0 else 0
         return func(j)-func(i-1)
         
 
 
 # Your NumArray object will be instantiated and called as such:
 # obj = NumArray(nums)
 # obj.update(i,val)
 # param_2 = obj.sumRange(i,j)
