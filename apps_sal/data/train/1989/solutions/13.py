class Solution:

    def longestAwesome(self, s: str) -> int:
        bd = {}
        bd[0] = -1
        soen = 0
        for (i, n) in enumerate(s):
            soen ^= 1 << int(n)
            bd[soen] = -1
            bd[soen] = i
            for j in range(10):
                soen_cpy = soen
                soen_cpy ^= 1 << j
                if soen_cpy in bd:
                    bd[soen_cpy] = i
        soen = 0
        max_ = bd[0] + 1
        for (i, n) in enumerate(s):
            soen ^= 1 << int(n)
            cur_max = bd[soen] - i
            if cur_max > max_:
                max_ = cur_max
        return max_
