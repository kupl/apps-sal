class Solution:
    def minCostConnectPoints(self, A: List[List[int]]) -> int:
        # [[0,0],[2,2],[3,10],[5,2],[7,0]]
        
                # edge[i].append([x+y,j])
                # edge[j].append([x+y,i])
        # print(edge)
        self.graph=[]
        def find(par,i):
            if par[i]==i:
                return i
            return find(par,par[i])

        def union(par, rank, x, y): 
            xroot = find(par, x) 
            yroot = find(par, y) 
            if rank[xroot] < rank[yroot]: 
                par[xroot] = yroot 
            elif rank[xroot] > rank[yroot]: 
                par[yroot] = xroot 
            else : 
                par[yroot] = xroot 
                rank[xroot] += 1


        def kruskal(): 

            result =[] #This will store the resultant MST 

            i = 0 # An index variable, used for sorted edges 
            e = 0 
            self.graph =  sorted(edges,key=lambda item: item[2]) 

            par = []
            rank = [] 

            # Create V subsets with single elements 
            for node in range(len(A)): 
                par.append(node) 
                rank.append(0) 

            # Number of edges to be taken is equal to V-1 
            while e < len(A) -1 : 

                # Step 2: Pick the smallest edge and increment  
                        # the index for next iteration 
                u,v,w =  self.graph[i] 
                i = i + 1
                x = find(par, u) 
                y = find(par ,v) 

                # If including this edge does't cause cycle,  
                            # include it in result and increment the index 
                            # of result for next edge 
                if x != y: 
                    e = e + 1     
                    result.append([u,v,w]) 
                    union(par, rank, x, y) 
            return result
            # Else discard the edge 
                
        edge=defaultdict(list)
        edges=[]
        
        
        for i in range(len(A)):
            for j in range(i+1,len(A)):
                x=abs(A[i][0]-A[j][0])
                y=abs(A[i][1]-A[j][1])
                edges.append([i,j,x+y])
        res=kruskal()
        main=0
        for i in res:
            main+=i[-1]
        return main


