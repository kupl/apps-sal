class Solution:
    def longestAwesome(self, s: str) -> int:
        N = len(s)
        M = 10
        prefix = [0 for _ in range(N + 1)]
        for i in range(1, N + 1):
            x = int(s[i - 1])
            prefix[i] = prefix[i - 1] ^ (1 << x)
        print('prefix', prefix)
        targets = [0]
        for i in range(M):
            mask = 1 << i
            targets.append(mask)
        print('targets', targets)
        seen = collections.defaultdict(int)
        ans = 0
        for i, p in enumerate(prefix):
            for target in targets:
                want = p ^ target
                if want not in seen:
                    continue
                k = seen[want]
                cand = i - k
                ans = max(ans, cand)
            if p not in seen:
                seen[p] = i
        return ans
