class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vow = set(list("aeiouAEIOU"))
        sList = list(s)

        sPrt = 0
        ePrt = len(sList) - 1

        while sPrt < ePrt:

            if sList[sPrt] in vow and sList[ePrt] in vow:
                sList[sPrt], sList[ePrt] = sList[ePrt], sList[sPrt]
                sPrt = sPrt + 1
                ePrt = ePrt - 1
            elif sList[sPrt] in vow:
                ePrt = ePrt - 1
            elif sList[ePrt] in vow:
                sPrt = sPrt + 1
            else:
                sPrt = sPrt + 1
                ePrt = ePrt - 1

        return "".join(sList)
