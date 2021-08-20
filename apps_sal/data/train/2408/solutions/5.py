class Solution:

    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        '\n         #complexity 2*len(s)\n         idx=-1\n         let_dict={}\n         for letter in s:\n             if letter not in let_dict:\n                 let_dict[letter]=1\n             else:\n                 let_dict[letter]+=1\n         \n         for i in range(len(s)):\n             if let_dict[s[i]]==1:\n                 idx=i\n                 break\n         return idx\n         '
        letters = 'abcdefghijklmnopqrstuvwxyz'
        indxs = [s.index(l) for l in letters if s.count(l) == 1]
        if len(indxs) > 0:
            return min(indxs)
        else:
            return -1
