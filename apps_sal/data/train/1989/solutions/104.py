class Solution:
    def longestAwesome(self, s: str) -> int:
        mem = {0: -1}
        res = 0
        state = 0
        for i, x in enumerate(s):
            idx = ord(x) - ord('0')
            state ^= (1 << idx)
            if state in mem:
                res = max(res, i - mem[state])

            for shift in range(10):
                tmp = state ^ (1 << shift)
                if tmp in mem:
                    res = max(res, i - mem[tmp])
            if state not in mem:
                mem[state] = i
        return res

