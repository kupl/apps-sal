class Solution:

    def longestAwesome(self, s: str) -> int:
        mask = {n: 1 << n for n in range(10)}
        target = [0] + list(mask.values())
        loc = [-2] * (1 << 10)
        for x in target:
            loc[x] = -1
        sofar = 0
        ans = 0
        for (idx, ch) in enumerate(s):
            m = mask[int(ch)]
            sofar = sofar ^ m
            if loc[sofar] > -2:
                ans = max(ans, idx - loc[sofar])
            for t in target:
                ntarget = sofar ^ t
                if loc[ntarget] == -2:
                    loc[ntarget] = idx
        return ans
