class Solution:
    def maxNumEdgesToRemove(self, n: int, A: List[List[int]]) -> int:
        g = collections.defaultdict(list)
        
        self.vis = {}
        
        compIdx = {}
        
        def dfs(node, typ, compIndex, mapRef = compIdx):
            mapRef[node] = compIndex
            self.vis[node] = 1
            for child, eType in g[node]:
                if eType in typ and child not in self.vis:
                    dfs(child, typ, compIndex, mapRef)
            self.vis[node] = 2

        ctr3 = 0
        ctr1, ctr2 = 0, 0
        set1 = set()
        set2 = set()
        set3 = set()
        for k,i,j in A:
            if k == 3:
                ctr3 += 1
                ctr1 += 1
                ctr2 += 1
                set3.add(i)
                set3.add(j)
            elif k == 1:
                ctr1 += 1
                set1.add(i)
                set1.add(j)
            else:
                ctr2 += 1
                set2.add(i)
                set2.add(j)
            g[i].append((j,k))
            g[j].append((i,k))
        
        comp3 = 0
        for node in set3:
            if node not in self.vis:
                dfs(node, [3], comp3)
                comp3 += 1
        
        # Deletable edges of type 3
        res1 = ctr3 - ((len(set3)) - comp3)
        
        comp1Idx = {}
        comp1 = 0
        self.vis = {}
        for node in set1.union(set3):
            if node not in self.vis:
                dfs(node, [1, 3], comp1, comp1Idx)
                comp1 += 1
        
        comp2Idx = {}
        comp2 = 0
        self.vis = {}
        for node in set2.union(set3):
            if node not in self.vis:
                dfs(node, [2, 3], comp2, comp2Idx)
                comp2 += 1
        
        print(comp1, comp2, comp3, len(comp1Idx), len(comp2Idx), len(compIdx), len(A))
        
        if comp1 > 1 or comp2 > 1 or len(comp1Idx) != n or len(comp2Idx) != n:
            return -1
        
        res2 = ctr1 - ((len(set3.union(set1))) - comp1)
        res3 = ctr2 - ((len(set3.union(set2))) - comp2)
        
        print(res1, res2, res3)
        return - res1 + res2 + res3
    
    
\"\"\"
13
[[1,1,2],[2,1,3],[3,2,4],[3,2,5],[1,2,6],[3,6,7],[3,7,8],[3,6,9],[3,4,10],[2,3,11],[1,5,12],[3,3,13],[2,1,10],[2,6,11],[3,5,13],[1,9,12],[1,6,8],[3,6,13],[2,1,4],[1,1,13],[2,9,10],[2,1,6],[2,10,13],[2,2,9],[3,4,12],[2,4,7],[1,1,10],[1,3,7],[1,7,11],[3,3,12],[2,4,8],[3,8,9],[1,9,13],[2,4,10],[1,6,9],[3,10,13],[1,7,10],[1,1,11],[2,4,9],[3,5,11],[3,2,6],[2,1,5],[2,5,11],[2,1,7],[2,3,8],[2,8,9],[3,4,13],[3,3,8],[3,3,11],[2,9,11],[3,1,8],[2,1,8],[3,8,13],[2,10,11],[3,1,5],[1,10,11],[1,7,12],[2,3,5],[3,1,13],[2,4,11],[2,3,9],[2,6,9],[2,1,13],[3,1,12],[2,7,8],[2,5,6],[3,1,9],[1,5,10],[3,2,13],[2,3,6],[2,2,10],[3,4,11],[1,4,13],[3,5,10],[1,4,10],[1,1,8],[3,3,4],[2,4,6],[2,7,11],[2,7,10],[2,3,12],[3,7,11],[3,9,10],[2,11,13],[1,1,12],[2,10,12],[1,7,13],[1,4,11],[2,4,5],[1,3,10],[2,12,13],[3,3,10],[1,6,12],[3,6,10],[1,3,4],[2,7,9],[1,3,11],[2,2,8],[1,2,8],[1,11,13],[1,2,13],[2,2,6],[1,4,6],[1,6,11],[3,1,2],[1,1,3],[2,11,12],[3,2,11],[1,9,10],[2,6,12],[3,1,7],[1,4,9],[1,10,12],[2,6,13],[2,2,12],[2,1,11],[2,5,9],[1,3,8],[1,7,8],[1,2,12],[1,5,11],[2,7,12],[3,1,11],[3,9,12],[3,2,9],[3,10,11]]
\"\"\"
