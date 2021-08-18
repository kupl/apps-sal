class Solution:
    def binaryGap(self, n: int) -> int:
        if n == 0:
            return 0

        while n & 1 == 0:
            n = n >> 1

        global_max = local_max = 0
        while n > 0:
            if n & 1 == 1:
                global_max = max(global_max, local_max)
                local_max = 1
            else:
                local_max += 1
            n = n >> 1

        return global_max
