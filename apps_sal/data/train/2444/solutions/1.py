class Solution:
    def binaryGap(self, n: int) -> int:
        bins = ''
        maxv = 0
        i = 0
        pre = None
        while n > 0:
            if n % 2 == 1:
                if pre is not None:
                    maxv = max(maxv, i - pre)
                pre = i
            n //= 2
            i += 1

        return maxv
