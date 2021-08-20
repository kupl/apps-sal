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

    def isOneBitCharacter(self, bits):
        parity = bits.pop()
        while bits and bits.pop():
            parity ^= 1
        return parity == 0

    def isOneBitCharacter(self, bits):
        i = 0
        while i < len(bits) - 1:
            i += bits[i] + 1
        return i == len(bits) - 1
