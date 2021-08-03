class Solution:
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        n = len(bits)
        i = 0
        current = 0

        while i < n:
            if bits[i] == 1:
                current = 2
                i += 2
            else:
                current = 1
                i += 1

        if current == 1:
            return True
        else:
            return False
