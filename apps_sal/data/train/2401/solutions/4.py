class Solution:

    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        strlst = str.split()
        return [pattern.find(i) for i in pattern] == [strlst.index(i) for i in strlst]
        '\n         my first solution...beat 93%\n         \n         strlst = str.split()\n         \n         if len(pattern) != len(strlst) or len(pattern) == 0:\n             return False\n         if len(pattern) == 1:\n             return True\n         \n         pdic = {}\n         pnum = []\n         sdic = {}\n         snum = []\n         i = 0\n         j = 0\n         k = 0\n         while i < len(pattern):\n             if pattern[i] not in pdic:\n                 pdic[pattern[i]] = j\n                 pnum.append(j)\n                 j += 1\n             else:\n                 pnum.append(pdic[pattern[i]])\n             if strlst[i] not in sdic:\n                 sdic[strlst[i]] = k\n                 snum.append(k)\n                 k += 1\n             else:\n                 snum.append(sdic[strlst[i]])\n             i += 1\n         \n         if pnum == snum:\n             return True\n         return False\n         '
