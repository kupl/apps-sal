class Solution:
     def dominantIndex(self, nums):
         """
         :type nums: List[int]
         :rtype: int
         """
         
         if len(nums) == 1:
             return 0
 
         doubleBigIndex = 0
         halfpoint = 0
         biggest = 0
         for index, item in enumerate(nums):
             print((biggest, halfpoint, doubleBigIndex, item))
             if item >= 2*biggest:
                 biggest = item
                 doubleBigIndex = index
                 halfpoint = biggest/2.0
             elif item > halfpoint:
                 doubleBigIndex = -1
             print(doubleBigIndex)
                 
         return doubleBigIndex
                 
             
                 

