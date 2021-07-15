class Solution:
     def complexNumberMultiply(self, a, b):
         """
         :type a: str
         :type b: str
         :rtype: str
         """
         
         aR = self.getReal(a)
         bR = self.getReal(b)
         aI = self.getImg(a)
         bI = self.getImg(b)
         
         real = aR * bR - aI * bI
         img = aR * bI + aI * bR
         
         return str(real) + "+" + str(img) + "i"
         
     
     
     def getReal(self, s):
         res = s[0]
         for char in s[1:]:
             if char == "+" or char == "-":
                 break
             else:
                 res += char
         
         return int(res)
     
     
     def getImg(self, s):
         res = ""
         pos = 0
         for i in range(1, len(s)):
             if s[i] == "+" or s[i] == "-":
                 pos = i + 1
                 break
     
         while s[pos] != "i":
             res += s[pos]
             pos += 1
         
         return int(res)
                     

