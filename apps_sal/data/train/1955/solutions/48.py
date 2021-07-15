class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n=len(s)
        m=len(pairs)
        
        ## If string length is 1 or less, or if there are no swappable pairs, return original string
        if n<=1 or m==0: return s
        
        ## Parent array for storing group parent ids in union find
        ## For each node, traversing upward would lead to the group leader.
        ## All connected indices share the same group leader
        parent= [i for i in range(n) ] 
        
        ## Returns the group leader index for the given index
        def find(i):
            pi = parent[i]
            while parent[pi] != pi :
                pi = parent[pi]
            parent[i] = pi
            return parent[i]
        
        ## Merges two indices into same group
        def union(i,j):
            pi=find(i)
            pj=find(j)
            if pi!=pj:
                parent[pj]=pi
        
        for index1,index2 in pairs:
            union(index1,index2)

        ## Forming groups or connected components
        groups={}
        for index in range(n):
            leader = find(index)
            groups[leader] = groups.get(leader,[])
            groups[leader].append(s[index])

        for leader in groups.keys():
            groups[leader].sort()

        group_index={}
        result=''
        for index in range(n):
            leader=find(index)
            group_index[leader]=group_index.get(leader,0)+1
            result+=groups[leader][group_index[leader]-1]
        return result     
