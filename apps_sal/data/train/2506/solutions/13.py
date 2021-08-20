class Solution:

    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        '\n    #    my second solution...modified based on first solution...\n         l = len(s)\n         \n         sdic = {}\n         snum = []\n         i = 0\n         j = 1\n         while i < l:\n             if s[i] not in sdic:\n                 sdic[s[i]] = j\n                 snum.append(j)\n                 j += 1\n             else:\n                 snum.append(sdic[s[i]])\n             i += 1\n             \n         tdic = {}\n         tnum = []\n         i = 0\n         j = 1\n         while i < l:\n             if t[i] not in tdic:\n                 if j != snum[i]:\n                     return False\n                 tdic[t[i]] = j\n                 tnum.append(j)\n                 j += 1\n             else:\n                 if tdic[t[i]] != snum[i]:\n                     return False\n                 tnum.append(tdic[t[i]])\n             i += 1\n         \n         return True\n         \n         \n         '
        sdic = {}
        snum = []
        i = 0
        j = 1
        while i < len(s):
            if s[i] not in sdic:
                sdic[s[i]] = j
                snum.append(j)
                j += 1
            else:
                snum.append(sdic[s[i]])
            i += 1
        tdic = {}
        tnum = []
        i = 0
        j = 1
        while i < len(t):
            if t[i] not in tdic:
                tdic[t[i]] = j
                tnum.append(j)
                j += 1
            else:
                tnum.append(tdic[t[i]])
            i += 1
        if snum == tnum:
            return True
        else:
            return False
