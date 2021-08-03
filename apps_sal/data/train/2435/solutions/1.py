class Solution:
    def generateTheString(self, n: int) -> str:
        if (n & 0x1) == 1:
            return 'a' * n
        else:
            return (n - 1) * 'a' + 'b'
