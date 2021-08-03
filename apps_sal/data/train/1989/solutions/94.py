class Solution:
    def longestAwesome(self, s: str) -> int:
        m = defaultdict(int)
        state = [0] * 10
        m[tuple(state)] = -1
        ans = 0
        for i, c in enumerate(s):
            k = int(c)
            state[k] = 1 - state[k]
            tstate = tuple(state)
            if tstate not in m:
                m[tstate] = i
            else:
                ans = max(ans, i - m[tstate])
            for n in range(10):
                state[n] = 1 - state[n]
                tstate = tuple(state)
                if tstate in m:
                    ans = max(ans, i - m[tstate])
                state[n] = 1 - state[n]
        return ans
