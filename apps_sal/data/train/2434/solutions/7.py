class Solution:
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        if len(bits) == 1 and bits[0] == 1:
            return False
        n = len(bits)
        i = 0
        while(i < n):
            if i == n - 1:
                return True
            else:
                if bits[i] == 1:
                    i += 2
                else:
                    i += 1
        return False
