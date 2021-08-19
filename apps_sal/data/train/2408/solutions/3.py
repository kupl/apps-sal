class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        """
         #complexity 2*len(s)
         idx=-1
         let_dict={}
         for letter in s:
             if letter not in let_dict:
                 let_dict[letter]=1
             else:
                 let_dict[letter]+=1
         
         for i in range(len(s)):
             if let_dict[s[i]]==1:
                 idx=i
                 break
         return idx
         """
        inp_set = 'abcdefghijklmnoprstuvwxyz'
        indxs = [s.index(l) for l in inp_set if s.count(l) == 1]
        if len(indxs) == 0:
            return -1
        else:
            return min(indxs)
