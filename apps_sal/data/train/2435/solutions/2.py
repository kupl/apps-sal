class Solution:

    def generateTheString(self, n: int) -> str:
        if n % 2 == 0:
            return 'a' * (n - 1) + 'b'
        elif n == 1:
            return 'a'
        else:
            return 'a' * (n - 2) + 'bc'
