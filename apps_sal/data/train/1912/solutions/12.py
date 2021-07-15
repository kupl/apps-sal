class Solution:
     def nextGreatestLetter(self, letters, target):
         """
         :type letters: List[str]
         :type target: str
         :rtype: str
         """
         minL = 'z'
         result = 'z'
         wrap = True
         for l in letters:
             minL = min(minL, l)
             if l > target:
                 wrap = False
                 result = min(result, l)
         if not wrap:
             return result
         else:
             return minL

