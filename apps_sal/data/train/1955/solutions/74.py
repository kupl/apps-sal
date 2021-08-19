class Solution:

    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        dd = {x: x for x in [i for v in pairs for i in v]}

        def merge(x, y):
            (x, y) = (find(x), find(y))
            if x != y:
                dd[x] = y

        def find(x):
            if dd[x] != x:
                dd[x] = find(dd[x])
            return dd[x]
        for (i, x) in pairs:
            merge(i, x)
        agg = collections.defaultdict(list)
        for i in dd:
            agg[find(i)].append(s[i])
        for i in agg:
            agg[i] = sorted(agg[i], reverse=1)
        s = list(s)
        for i in range(len(s)):
            if i in dd:
                s[i] = agg[find(i)].pop()
        return ''.join(s)
