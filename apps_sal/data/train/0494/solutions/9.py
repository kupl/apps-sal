class Solution:
    import random

    def longestDecomposition(self, text: str) -> int:

        def check_eq(s, st1, st2, mx):
            while s[st1] == s[st2]:
                st1 += 1
                st2 += 1
                if st1 == mx:
                    return True
            return False
        if len(text) == 1:
            return 1
        ln = len(text)
        a = (1, -1)
        b = (1, -1)
        hsh_st = 0
        hsh_ed = 0
        ln_ch = 0
        for i in range(1, (ln >> 1) + 1):
            ln_ch += 1
            st1 = b[1] + 1
            hsh_st += ord(text[i - 1])
            st2 = ln - i
            hsh_ed += ord(text[st2])
            total = st1 + ln_ch
            res = False
            if hsh_st == hsh_ed:
                res = check_eq(text, st1, st2, total)
            if res:
                (b, a) = ((b[0] + 2, i - 1), b)
                ln_ch = 0
                hsh_st = 0
                hsh_ed = 0
            else:
                (b, a) = (b, b)
        if b[0] > a[0] and b[0] > 1 and (len(text) % 2 == 0):
            return b[0] - 1
        return b[0]
