class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        g = collections.defaultdict(list)
        for a, b in pairs:
            g[a].append(b)
            g[b].append(a)

        def find(i, idx):
            for k in g[i]:
                if not visited[k]:
                    visited[k] = 1
                    idx.append(k)
                    find(k, idx)
        n = len(s)
        s = list(s)
        visited = [0] * n
        for i in range(n):
            if visited[i]:
                continue
            visited[i] = 1
            idx = [i]
            find(i, idx)
            idx.sort()
            chars = [s[j] for j in idx]
            chars.sort()
            for j, c in zip(idx, chars):
                s[j] = c
        return ''.join(s)
