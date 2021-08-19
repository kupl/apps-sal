class Solution:

    def longestAwesome(self, s: str) -> int:
        N = len(s)
        prefix = [0 for _ in range(N + 1)]
        for (i, value) in enumerate(s):
            x = int(value)
            prefix[i + 1] = prefix[i] ^ 1 << x
        valids = set([0])
        for i in range(10):
            valids.add(1 << i)
        ans = 0
        seen = collections.defaultdict(int)
        for (j, q) in enumerate(prefix):
            for target in valids:
                want = q ^ target
                if want not in seen:
                    continue
                i = seen[want]
                ans = max(ans, j - i)
            if q not in seen:
                seen[q] = j
        return ans
