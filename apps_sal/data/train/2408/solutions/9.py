class Solution:

    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        '\n         dict1 = {}\n         dict2 = {}\n         lst = []\n         \n         for i in range(len(s)):\n             dict1[s[i]] = dict1.get(s[i],0) + 1\n             if s[i] not in dict2.keys():\n                 dict2[s[i]] = i\n         \n         for key in dict1.keys():\n             if dict1[key] == 1:\n                 lst.append(dict2[key])\n         \n         lst.sort()\n         if len(lst) > 0:\n             return lst[0]\n         return -1\n         '
        letters = 'abcdefghijklmnopqrstuvwxyz'
        lst = [s.index(l) for l in letters if s.count(l) == 1]
        if len(lst) > 0:
            return min(lst)
        else:
            return -1
