class Solution:

    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        bits = ''.join(map(str, bits))
        return self.dfs(bits)

    def dfs(self, bits):
        if len(bits) == 0:
            return False
        elif len(bits) == 1:
            if bits[0] == '0':
                return True
        else:
            if bits[:2] == '10':
                if self.dfs(bits[2:]):
                    return True
            elif bits[:2] == '11':
                if self.dfs(bits[2:]):
                    return True
            elif bits[0] == '0':
                if self.dfs(bits[1:]):
                    return True
            return False
