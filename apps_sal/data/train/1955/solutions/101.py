class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        class UF:
            def __init__(self, n): self.p = list(range(n))
            def union(self, x, y): self.p[self.find(x)] = self.find(y)

            def find(self, x):
                if x != self.p[x]:
                    self.p[x] = self.find(self.p[x])
                return self.p[x]

        union_find, result, group = UF(len(s)), [], defaultdict(list)
        for pair in pairs:
            union_find.union(pair[0], pair[1])
        for i in range(len(s)):
            union_find.p[i] = union_find.find(i)
        for i in range(len(s)):
            group[union_find.find(i)].append(s[i])
        for comp_id in list(group.keys()):
            group[comp_id].sort(reverse=True)
        for i in range(len(s)):
            result.append(group[union_find.find(i)].pop())
        return ''.join(result)
