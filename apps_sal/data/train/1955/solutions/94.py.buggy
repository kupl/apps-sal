class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        uf = {}
        
        def find(x):
            uf.setdefault(x, x)
            if uf[x] != x:
                uf[x] = find(uf[x])
            return uf[x]
        
        def union(x, y):
            uf[find(x)] = find(y)
            
        for a, b in pairs:
            union(a, b)
            
        ans = [\"\"] * len(s)
        dic = collections.defaultdict(list)
        for i, ss in enumerate(s):
            dic[find(i)].append((ss, i))
        print(dic)
        for d in dic:
            for ss, i in zip(sorted(ss for ss, i in dic[d]), sorted(i for ss, i in dic[d])):
                ans[i] = ss
        return \"\".join(ans)
                
                
            
            
            
            
            
            
            
