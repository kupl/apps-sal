class Solution:

    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        p = list(range(len(s)))
        d = defaultdict(list)

        def find(x):
            if x != p[x]:
                p[x] = find(p[x])
            return p[x]

        def union(x, y):
            p[find(x)] = find(y)
        for (a, b) in pairs:
            union(a, b)
        for i in range(len(p)):
            d[find(i)].append(s[i])
        for x in d:
            d[find(x)].sort(reverse=True)
        ret = ''
        for i in range(len(s)):
            ret += d[find(i)].pop()
        return ret
