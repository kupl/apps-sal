class Solution:

    def longestAwesome(self, s: str) -> int:
        cum = [0]
        firsts = {0: -1}
        lasts = {0: -1}
        for (i, c) in enumerate(s):
            cum.append(cum[-1] ^ 1 << ord(c) - 48)
            if cum[-1] not in firsts:
                firsts[cum[-1]] = i
            lasts[cum[-1]] = i
        mx = 1
        for k in firsts:
            mx = max(mx, lasts[k] - firsts[k])
            for off in range(10):
                o = k ^ 1 << off
                if o in firsts:
                    mx = max(mx, lasts[o] - firsts[k])
        return mx
