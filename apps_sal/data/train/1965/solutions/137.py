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
        
        subsets1 = ['1 index'] + [[x+1,0] for x in range(n)] #Alice's unionfind
        subsets2 = ['1 index'] + [[x+1,0] for x in range(n)] #Bob's unionfind
        
        #edges = sorted(edges, key= lambda e: -e[0])
        e = 0 #number of total edges used
        e1 = 0 #number of edges for Alice
        e2 = 0 #number of edges for Bob
        i = 0 #track position in edges list
        
        #start with type 3 edges
        while e < n - 1:
            if i == len(edges): 
                i = 0
                break
            typ, u, v = edges[i]
            if typ != 3: 
                i += 1
                continue
            if find(subsets1, u) != find(subsets1, v):
                union(subsets1, u, v)
                e += 1
            
            i += 1
        
        #everything that was done to Alice applies to Bob
        e1 = e
        e2 = e
        subsets2 = copy.deepcopy(subsets1)
        i=0
        #once done with shared edges, do Bob's
        while e2 < n-1:
            if i == len(edges): 
                i = 0
                break
            typ, u, v = edges[i]
            if typ != 2: 
                i+=1
                continue
            if find(subsets2, u) != find(subsets2, v):
                union(subsets2, u, v)
                e += 1
                e2 += 1
            i += 1
        
        if e2 < n - 1: 
            return -1 #if we've used all edges bob can use (types 2 and 3) and he still can't reach all nodes, ur fucked
        
        i=0
        #now finish Alice's MST
        while e1 < n-1:
            if i == len(edges): 
                return -1
        
            typ, u, v = edges[i]
            if typ != 1: 
                i += 1
                continue
            
            if find(subsets1, u) != find(subsets1, v):
                union(subsets1, u, v)
                e += 1
                e1 += 1
            i += 1
            
        return len(edges) - e
            
            
            
            
        
        

