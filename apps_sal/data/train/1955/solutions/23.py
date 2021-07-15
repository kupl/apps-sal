class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        parents = [i for i,_ in enumerate(s)]
        def find(i):
            if i == parents[i]:
                return i
            parents[i] = find(parents[i])
            return parents[i]
        
        def union(i, j):
            i, j = find(i), find(j)
            if i != j:
                parents[i] = parents[j]
            
        for i,j in pairs:
            union(i,j)
                           
        groups = reduce((lambda group, i:
                group[find(i)].append(i)
               or group),
               range(len(s)),
              defaultdict(list))
        
        res = [0] * len(s)
        for items in groups.values():
            for i,c in zip(items, sorted(s[i] for i in items)):
                res[i] = c
            
        return ''.join(res)
