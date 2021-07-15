class Solution:
    def longestAwesome(self, s: str) -> int:
        N = len(s)
        prefix = [0 for _ in range(N + 1)]
        for i in range(1, N + 1):
            x = int(s[i - 1])
            prefix[i] = prefix[i - 1] ^ (1 << x)
        valids = [0]
        for i in range(10):
            valids.append(1 << i)
        seen = collections.defaultdict(int)
        ans = 0
        for i, p in enumerate(prefix):
            for valid in valids:
                want = p ^ valid
                if want not in seen:
                    continue
                k = seen[want]
                cand = i - k
                ans = max(ans, cand)
            if p not in seen:
                seen[p] = i
        return ans
