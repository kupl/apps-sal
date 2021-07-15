import collections
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        s=list(s)
        path=collections.defaultdict(list)
        for u,v in pairs:
            path[u].append(v)
            path[v].append(u)
        seen=set()
        group=[] # group of nodes
        for i in range(len(s)):
            if i in seen: continue 
            else: # start to search for connected points
                cur=[i]
                connect=[i]
                while cur:
                    temp=[]
                    for c in cur:
                        if c not in seen: 
                            seen.add(c)
                            temp+=[x for x in path[c] if x not in seen]
                    cur=temp
                    connect+=cur
                group.append(connect)
        for g in group:
            temp=sorted([s[i] for i in set(g)])
            for i in sorted(set(g)):
                s[i]=temp[0]
                temp.pop(0)
        return \"\".join(s)
             
                
            
            
        
        
