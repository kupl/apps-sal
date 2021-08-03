class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        pr = [i for i in range(len(s))]

        def union(x, y):
            p1 = find(x)
            p2 = find(y)
            if p1 != p2:
                pr[p1] = p2

        def find(x):
            while pr[x] != x:
                pr[x] = pr[pr[x]]
                x = pr[x]
            return x

        for i in pairs:
            union(i[0], i[1])

        from collections import defaultdict
        dp = defaultdict(list)
        for i in range(len(s)):
            ld = find(i)
            dp[ld].append(i)
        ans = [0] * len(s)
        for i in dp:
            dp[i].sort()
            st = ''
            for j in dp[i]:
                st += s[j]
            st = sorted(st)
            c = 0
            for j in dp[i]:
                ans[j] = st[c]
                c += 1
        return ''.join(ans)
