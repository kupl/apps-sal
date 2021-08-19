class Solution:

    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        l = len(bits)
        if l == 1:
            if bits[0] == 0:
                return True
            else:
                return False
        i = 0
        while 1:
            if bits[i] == 1:
                l -= 2
                i += 2
            else:
                l -= 1
                i += 1
            if l == 1:
                return True
            if l == 0:
                return False
