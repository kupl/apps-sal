class Solution:
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """

        strlst = str.split()
        return [pattern.find(i) for i in pattern] == [strlst.index(i) for i in strlst]

        """
         my first solution...beat 93%
         
         strlst = str.split()
         
         if len(pattern) != len(strlst) or len(pattern) == 0:
             return False
         if len(pattern) == 1:
             return True
         
         pdic = {}
         pnum = []
         sdic = {}
         snum = []
         i = 0
         j = 0
         k = 0
         while i < len(pattern):
             if pattern[i] not in pdic:
                 pdic[pattern[i]] = j
                 pnum.append(j)
                 j += 1
             else:
                 pnum.append(pdic[pattern[i]])
             if strlst[i] not in sdic:
                 sdic[strlst[i]] = k
                 snum.append(k)
                 k += 1
             else:
                 snum.append(sdic[strlst[i]])
             i += 1
         
         if pnum == snum:
             return True
         return False
         """
