from collections import defaultdict


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:

        def find(node):
            path = []
            while root[node] != node:
                path.append(node)
                node = root[node]

            for n in path:
                root[n] = node
            return node

        def union(a, b):
            r1, r2 = find(a), find(b)
            if r1 != r2:
                root[r1] = r2

        root = {i: i for i in range(len(s))}
        for a, b in pairs:
            union(a, b)

        root_to_char = defaultdict(list)
        for k in list(root.keys()):
            root_to_char[find(k)].append(s[k])

        for v in list(root_to_char.values()):
            v.sort(reverse=True)

        res = []
        for i in range(len(s)):
            res.append(root_to_char[root[i]].pop())

        return ''.join(res)
