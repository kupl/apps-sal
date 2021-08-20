class Solution:

    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        parent = [i for i in range(n)]
        group = collections.defaultdict(list)
        res = []

        def find(a):
            p = parent[a]
            while p != parent[p]:
                p = parent[p]
            parent[a] = p
            return p

        def union(a, b):
            (pa, pb) = (find(a), find(b))
            if pa != pb:
                parent[pa] = pb
        for (u, v) in pairs:
            union(u, v)
        for i in range(n):
            group[find(i)].append(s[i])
        for k in group:
            group[k].sort(reverse=True)
        for i in range(n):
            res.append(group[find(i)].pop())
        return ''.join(res)
