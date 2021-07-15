class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        '''always keep type 3 if possible'''
        edges123 = [[]  for _ in range(3) ] 
        for t, a, b in edges: edges123[t-1].append( (a-1,b-1) )
        # type 0 1 2 for alice, bob and both
        self.res = 0
        Parents = [[i for i in range(n)] for _ in range(2) ]
        depth = [[1]*n for _ in range(2)]
        selectedEdges = [0,0]
        def FindRoot(n,t):
            #print('node',n,'type',t)
            if Parents[t][n] != n:
                Parents[t][n] = FindRoot(Parents[t][n] ,t)
            return Parents[t][n] 
        def Uni(x,y,t):
            rx, ry = FindRoot(x,t), FindRoot(y,t)
            if rx == ry: return 0
            else:
                if depth[t][rx] >= depth[t][ry]:
                    Parents[t][ry] = rx
                    depth[t][rx] = max(depth[t][rx],depth[t][ry])
                else:
                    Parents[t][rx] = ry
                return 1
            
        def connect(thetype):
            mytypes = [thetype] if thetype < 2 else [ 0, 1 ]
            for x, y in edges123[thetype]:
                if all(Uni(x,y,t) for t in mytypes):
                    for t in mytypes: selectedEdges[t] += 1
                else:
                    self.res += 1
            # for t in mytypes: 
            #     root = [FindRoot(i,t) for i in range(n)]
            #     print(thetype,t, 'parents',Parents[t],root,selectedEdges,self.res)
                
        connect(2)
        connect(0)
        connect(1)
        return self.res if all(selectedEdges[t]==n-1 for t in [0,1]) else -1

