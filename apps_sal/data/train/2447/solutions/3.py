class Solution:
     def reverseVowels(self, s):
         """
         :type s: str
         :rtype: str
         """
         
         if len(s) <= 1:
             return s
         arr = list(s)
         vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
         
         left = 0
         right = len(s) - 1
         
         while right > left:
             
             
             while left < len(s) and s[left] not in vowels:
                 left += 1
             
             while right > 0 and s[right] not in vowels:
                 right -= 1
             
             if right <= left or right == 0 or left == len(s):
                 break
                 
             arr[left], arr[right] = arr[right], arr[left]
             right -= 1
             left += 1
             
         return ''.join(arr)
         
             
             
             
         
         

