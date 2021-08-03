class Solution:
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        bits.insert(0, 0)
        for i in range(len(bits) - 2, -1, -1):
            if bits[i] == 0 or i == 0:
                return (len(bits) - i) % 2 == 0
