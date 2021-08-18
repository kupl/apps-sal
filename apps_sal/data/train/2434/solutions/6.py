class Solution:
    def isOneBitCharacter(self, bits):
        n = len(bits)
        if bits[n - 1] != 0:
            return False
        else:
            i = 0
            while i < n - 2:
                print((bits[i], ', '))
                if bits[i] == 1:
                    if bits[i + 1] == 0 or bits[i + 1] == 1:
                        i += 1
                    else:
                        return False
                elif bits[i] == 0:
                    pass
                i += 1
            if bits[i] == 1:
                return False
            return True
