class Solution:
    def longestAwesome(self, s: str) -> int:
        df, dl = {}, {}
        df[0] = -1
        sm = 0
        res = 1
        for i, c in enumerate(s):
            sm ^= 1 << int(c)
            if sm not in df:
                df[sm] = i
            dl[sm] = i
        for fk, fv in df.items():
            for lk, lv in dl.items():
                if lv > fv:
                    xor = fk ^ lk
                    if xor == 0 or (xor & (xor - 1)) == 0:
                        res = max(res, lv - fv)
        return res
