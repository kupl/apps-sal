class Solution:
     def isValid(self, s):
         """
         :type s: str
         :rtype: bool
         """
         
         # ###method1
         # while  "()" in s or "[]" in s or "{}" in s:
         #     s = s.replace("()","").replace("[]","").replace("{}","")
         # return len(s)==0
         
         stack = []
         dict = {")":"(", "]":"[", "}":"{"}
         for char in s:
             if char in list(dict.values()):
                 stack.append(char)
             elif char in list(dict.keys()):
                 if stack==[] or dict[char] != stack.pop():
                     return False
             else:
                 return False
         return stack==[]
     
  

