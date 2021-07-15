class NumArray:
 
     def __init__(self, nums):
         """
         :type nums: List[int]
         """
         self.segTree = [0 for _ in range(len(nums) * 2)]
         self.build(nums)
         self.n = len(nums)
         
     def build(self, nums):
         n = len(nums)
         self.segTree[n: 2 * n] = nums[:]
         for i in range(n - 1, 0, -1):
             self.segTree[i] = self.eval(self.segTree[2 * i], self.segTree[2 * i + 1])
             
     def eval(self, x1, x2):
         return x1 + x2
 
     def update(self, i, val):
         """
         :type i: int
         :type val: int
         :rtype: void
         """
         k = i + self.n
         delta = val - self.segTree[k]
         while k > 0:
             self.segTree[k] += delta
             k //= 2
         
 
     def sumRange(self, i, j):
         """
         :type i: int
         :type j: int
         :rtype: int
         """
         l = i + self.n
         r = j + self.n 
         s = 0
         while l <= r:
             if l & 1 == 1:
                 s += self.segTree[l]
                 l += 1
             if r & 1 == 0:
                 s += self.segTree[r]
                 
             r -= 1
             l >>= 1
             r >>= 1
         return s
         
 
 
 # Your NumArray object will be instantiated and called as such:
 # obj = NumArray(nums)
 # obj.update(i,val)
 # param_2 = obj.sumRange(i,j)

