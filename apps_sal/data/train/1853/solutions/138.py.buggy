class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        map = collections.defaultdict(list)
        for f, t, w in edges:
            map[f].append((t, w))
            map[t].append((f, w))
        stack = []
        empty = -float(\"inf\")
        res = 0
        seen = []
        for i in range(n):
            seen.append(collections.defaultdict(int))
            stack.append((i, i, 0))
            if i not in map:
                empty = i
        if empty != -float(\"inf\"):
            return empty
        while stack:
            f, t, w = stack.pop()
            for a, b in map[t]:
                if a not in seen[f] and w + b <= distanceThreshold and a != f:
                    seen[f][a] = w + b
                    stack.append((f, a, w + b))
                elif a in seen[f] and w + b <= seen[f][a] and a != f:
                    seen[f][a] = w + b
                    stack.append((f, a, w + b))
        l = float(\"inf\")
        for k in range(len(seen)):
            if len(seen[k]) <= l:
                l = len(seen[k])
                res = k
        return res
