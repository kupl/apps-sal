class Solution:
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        n = 0
        for i in range(-2, -len(bits) - 1, -1):
            if bits[i] == 1:
                n += 1
            else:
                break
        return n % 2 == 0
