class Solution:
     def isAnagram(self, s, t):
         """
         :type s: str
         :type t: str
         :rtype: bool
         """
         ls = self.makeDict(s)
         lt = self.makeDict(t)
         if len(list(ls.keys())) > len(list(lt.keys())):
             for ks, vs in list(ls.items()):
                 if not ((ks in lt) and (lt[ks] == vs)):
                     return False
             return True
         else:
             for kt, vt in list(lt.items()):
                 if not ((kt in ls) and (ls[kt] == vt)):
                     return False
             return True
         
                
     def makeDict(self, s):
         ls = {}
         for l in s:
             if l in ls:
                 ls[l] += 1
             else:
                 ls[l] = 1
         return ls
         

