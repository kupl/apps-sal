class Solution:

    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        d = {}
        for (a, b) in pairs:
            if a not in d:
                d[a] = []
            if b not in d:
                d[b] = []
            d[a].append(b)
            d[b].append(a)

        def dfs(x, result):
            if x in d:
                result.append(x)
                for y in d.pop(x):
                    dfs(y, result)
        s = list(s)
        while d:
            x = next(iter(d))
            result = []
            dfs(x, result)
            result = sorted(result)
            B = sorted([s[i] for i in result])
            for (i, b) in enumerate(B):
                s[result[i]] = b
        return ''.join(s)
