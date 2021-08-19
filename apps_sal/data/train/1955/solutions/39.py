class Solution:

    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        par = {i: i for i in range(len(s))}

        def find(x):
            if par[x] != x:
                par[x] = find(par[x])
            return par[x]

        def union(x, y):
            (rx, ry) = (find(x), find(y))
            if rx != ry:
                par[rx] = ry
        for (x, y) in pairs:
            union(x, y)
        group2chars = defaultdict(list)
        for (idx, char) in enumerate(s):
            gid = find(idx)
            group2chars[gid].append(char)
        for gid in group2chars:
            group2chars[gid].sort(reverse=True)
        outstr = ''
        for (idx, char) in enumerate(s):
            gid = find(idx)
            outchar = group2chars[gid].pop()
            outstr += outchar
        return outstr
