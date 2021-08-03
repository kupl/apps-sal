class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        
        
        node = {i : i for i in range(len(s))}
        

        def find(x):
            if x != node[x]:
                node[x] = find(node[x])   
                
            return node[x]
        
        def union(x, y):
            if find(x) != find(y):
                node[find(x)] = find(y)
                
        ans = []
        m = defaultdict(list)
        
        for x, y in pairs:
            union(x, y)
        for i in range(len(s)):
            m[find(i)].append(s[i])
           
        for cid in m.keys():
            m[cid].sort(reverse=True)
        print(m.items())
            
        for  i in range(len(s)):
            ans.append(m[find(i)].pop())
            
        return \"\".join(ans)
            
            
                
        
        
        
        
     
