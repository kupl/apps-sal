from heapq import *


class Solution:
    def smallestStringWithSwaps(self, s: str, prs: List[List[int]]) -> str:
        f, m, ans = {}, defaultdict(list), []
        for p in prs:
            r_a, r_b = self.fnd(f, p[0]), self.fnd(f, p[1])
            if r_a != r_b:
                f[r_b] = r_a

        for i in range(len(s)):
            m[self.fnd(f, i)].append(s[i])
        for v in list(m.values()):
            heapify(v)
        for i in range(len(s)):
            ans.append(heappop(m[self.fnd(f, i)]))
        return ''.join(ans)

    def fnd(self, f, n):
        f[n] = f.get(n, n)
        if f[n] == n:
            return n
        f[n] = self.fnd(f, f[n])

        return f[n]
