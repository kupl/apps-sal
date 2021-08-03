class Solution:
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        i = len(bits)
        res = False
        while bits != []:
            e = bits.pop(0)
            if bits == [] and e == 0:
                return True
            if e == 1 and bits != []:
                bits.pop(0)
            i -= 1
        return res
