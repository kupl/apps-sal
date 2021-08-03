class Solution:
    def bitwiseComplement(self, N: int) -> int:

        if N == 0:
            return 1

        dummy_num = N

        n = 0
        while(dummy_num):
            n += 1
            dummy_num >>= 1

        ans = 0

        for i in range(n - 1, -1, -1):

            if (N >> i) & 1 == 0:
                ans |= (1 << i)

        return ans
