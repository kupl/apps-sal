class Solution:

    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        i = 0
        while i < len(bits) - 1:
            if bits[i] == 0:
                i += 1
            elif bits[i] == 1:
                i += 2
        return i == len(bits) - 1
