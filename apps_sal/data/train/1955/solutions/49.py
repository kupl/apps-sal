class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        parent = [i for i in range(n)]
        def find(i):
            if not i ==parent[i]:
                parent[i]=find(parent[i])
            return parent[i]    
        def union(i, j):
            a = find(i)
            b = find(j)
            parent[a] = b
        for i, j in pairs:
            union(i, j)
        memo = collections.defaultdict(list)
        for i in range(n):
            memo[find(i)].append(s[i])
        for k in memo.keys():
            memo[k].sort(reverse=True)
        res = []
        for i in range(n):
            res.append(memo[find(i)].pop())
        return \"\".join(res) 
