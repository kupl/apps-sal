class Solution:
    def linear(self, s):
        ans = 0
        d = {0: -1}
        mask = 0
        for i, c in enumerate(s):
            mask = (1 << int(c)) ^ mask

            if mask in d:
                ans = max(ans, i - d[mask])

            for j in range(32):
                s = mask ^ (1 << j)
                if s in d:
                    ans = max(ans, i - d[s])

            if mask not in d:
                d[mask] = i
        return ans

    def longestAwesome(self, s: str) -> int:
        return self.linear(s)

        ans = 0
        for i in range(len(s)):
            d = collections.defaultdict(int)
            odds = set()
            for j in range(i, len(s)):
                d[s[j]] += 1
                if d[s[j]] % 2:
                    odds.add(s[j])
                else:
                    if s[j] in odds:
                        odds.remove(s[j])

                if len(odds) <= 1:
                    ans = max(ans, j - i + 1)
        return ans
