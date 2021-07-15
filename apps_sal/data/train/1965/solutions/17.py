import copy

def union(subsets, u, v):
    uroot = find(subsets, u)
    vroot = find(subsets, v)
    
    if subsets[uroot][1] > subsets[vroot][1]:
        subsets[vroot][0] = uroot
    if subsets[vroot][1] > subsets[uroot][1]:
        subsets[uroot][0] = vroot
    if subsets[uroot][1] == subsets[vroot][1]:
        subsets[vroot][0] = uroot
        subsets[uroot][1] += 1
    

def find(subsets, u):
    if subsets[u][0] != u:
        subsets[u][0] = find(subsets, subsets[u][0])
    return subsets[u][0]


class Solution:
    #kruskal's
    #1 is alice and 2 is bob
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        
        mst1 = set() #set for Alice's MST
        mst2 = set() #set for Bob's MST
        subsets1 = ['1 index'] + [[x+1,0] for x in range(n)] #Alice's unionfind
        subsets2 = ['1 index'] + [[x+1,0] for x in range(n)] #Bob's unionfind
        
        edges = sorted(edges, key= lambda e: -e[0])
        e = 0 #number of total edges used
        e1 = 0 #number of edges for Alice
        e2 = 0 #number of edges for Bob
        i = 0 #track position in edges list
        
        #start with type 3 edges
        while e < n - 1:
            if i == len(edges): 
                return -1
            typ, u, v = edges[i]
            if typ != 3: break
            if find(subsets1, u) != find(subsets1, v):
                union(subsets1, u, v)
                mst1.add(u)
                mst1.add(v)
                e += 1
            
            i += 1
        
        #everything that was done to Alice applies to Bob
        e1 = e
        e2 = e
        mst2 = mst1.copy()
        subsets2 = copy.deepcopy(subsets1)
        
        #once done with shared edges, do Bob's
        while e2 < n-1:
            if i == len(edges): 
                return -1
            typ, u, v = edges[i]
            if typ != 2: break
            if find(subsets2, u) != find(subsets2, v):
                union(subsets2, u, v)
                mst2.add(u)
                mst2.add(v)
                e += 1
                e2 += 1
            i += 1
        
        if len(mst2) < n: 
            return -1 #if we've used all edges bob can use (types 2 and 3) and he still can't reach all nodes, ur fucked
        
        #now finish Alice's MST
        while e1 < n-1:
            if i == len(edges): 
                return -1
            
            typ, u, v = edges[i]
            if find(subsets1, u) != find(subsets1, v):
                union(subsets1, u, v)
                
                e += 1
                e1 += 1
            i += 1
            
        return len(edges) - e
            
            
            
            
        
        

