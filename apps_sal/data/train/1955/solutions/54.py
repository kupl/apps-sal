from typing import List


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        g = [[] for _ in range(len(s))]
        for edge in pairs:
            g[edge[0]].append(edge[1])
            g[edge[1]].append(edge[0])

        visited = set()

        def f(i):
            if i in visited:
                return
            else:
                visited.add(i)

            idxes.append(i)
            chars.append(s[i])

            for adj in g[i]:
                f(adj)

        ans = [''] * len(s)
        for i in range(len(s)):
            if i in visited:
                continue
            idxes = []
            chars = []
            f(i)

            idxes.sort()
            chars.sort()

            for j in range(len(chars)):
                ans[idxes[j]] = chars[j]

        return ''.join(ans)
