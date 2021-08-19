from typing import List


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        # build graph
        g = [[] for _ in range(len(s))]
        for edge in pairs:
            g[edge[0]].append(edge[1])
            g[edge[1]].append(edge[0])  # bug: 應為 indirected graph

        # DFS, find components
        visited = set()

        def f(i):  # fulfill idexes and chars
            if i in visited:
                return
            else:
                visited.add(i)

            # visit
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

            # sort each components
            idxes.sort()
            chars.sort()

            for j in range(len(chars)):
                ans[idxes[j]] = chars[j]

        return ''.join(ans)
