class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        parent = {i: i for i in range(len(s))}

        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]

        for edge in pairs:
            parent[find(edge[0])] = find(edge[1])

        parent_table = collections.defaultdict(list)
        for i in list(parent.keys()):
            parent_table[find(i)].append(i)

        ans = list(s)
        for i in list(parent_table.keys()):
            ids = sorted(parent_table[i])
            t = sorted(ans[j] for j in ids)
            for j in range(len(ids)):
                ans[ids[j]] = t[j]

        return ''.join(ans)
