class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        e3 = set([(x[1],x[2]) for x in edges if x[0] == 3])
        e2 = set([(x[1],x[2]) for x in edges if x[0] == 2])
        e1 = set([(x[1],x[2]) for x in edges if x[0] == 1])
        from collections import defaultdict 
        print(len(e3),len(e2),len(e1))
        #Class to represent a graph 
        class Graph: 

            def __init__(self,vertices): 
                self.V= vertices #No. of vertices 
                self.graph = [] # default dictionary  
                                        # to store graph 


            # function to add an edge to graph 
            def addEdge(self,u,v,w): 
                self.graph.append([u,v,w]) 

            # A utility function to find set of an element i 
            # (uses path compression technique) 
            def find(self, parent, i): 
                if parent[i] == i: 
                    return i 
                return self.find(parent, parent[i]) 

            # A function that does union of two sets of x and y 
            # (uses union by rank) 
            def union(self, parent, rank, x, y): 
                xroot = self.find(parent, x) 
                yroot = self.find(parent, y) 

                # Attach smaller rank tree under root of  
                # high rank tree (Union by Rank) 
                if rank[xroot] < rank[yroot]: 
                    parent[xroot] = yroot 
                elif rank[xroot] > rank[yroot]: 
                    parent[yroot] = xroot 

                # If ranks are same, then make one as root  
                # and increment its rank by one 
                else : 
                    parent[yroot] = xroot 
                    rank[xroot] += 1

            # The main function to construct MST using Kruskal's  
                # algorithm 
            def KruskalMST(self): 

                result =[] #This will store the resultant MST 
                rem = []

                i = 0 # An index variable, used for sorted edges 
                e = 0 # An index variable, used for result[] 

                    # Step 1:  Sort all the edges in non-decreasing  
                        # order of their 
                        # weight.  If we are not allowed to change the  
                        # given graph, we can create a copy of graph 
                self.graph =  sorted(self.graph,key=lambda item: item[2]) 
                print(\"l\",len(self.graph))

                parent = [] ; rank = [] 

                # Create V subsets with single elements 
                for node in range(self.V): 
                    parent.append(node) 
                    rank.append(0) 

                # Number of edges to be taken is equal to V-1
                notenough = False
                while e < self.V -1 : 
                    
                    # Step 2: Pick the smallest edge and increment  
                            # the index for next iteration 
                    #print(i)
                    try:
                        u,v,w =  self.graph[i]
                    except:
                        notenough = True
                        print(\"break\")
                        break
                    #print(i,u,v,e)
                    i = i + 1
                    x = self.find(parent, u) 
                    y = self.find(parent ,v) 

                    # If including this edge does't cause cycle,  
                                # include it in result and increment the index 
                                # of result for next edge 
                    if x != y: 
                        e = e + 1     
                        result.append([u,v,w]) 
                        self.union(parent, rank, x, y)             
                    # Else discard the edge
                    #else:
                        #rem.append((u,v))
                return result
                # print the contents of result[] to display the built MST 
                #print(\"Following are the edges in the constructed MST\")
                #for u,v,weight  in result: 
                    #print str(u) + \" -- \" + str(v) + \" == \" + str(weight) 
                    #print (\"%d -- %d == %d\" % (u,v,weight)) 
        # Driver code
        print(\"---\")
        g3 = Graph(n) 
        #e3.add((1,3))
        for e in e3:
            #print(e)
            g3.addEdge(e[0]-1,e[1]-1,1) 
            
        res = g3.KruskalMST()
        ret = len(e3) - len(res)
        e3 = set([(x[0]+1,x[1]+1) for x in res])
        print(\"g3\",ret,len(res), len(e3))
        
        
        g2 = Graph(n)
        for e in e3:
            g2.addEdge(e[0]-1,e[1]-1,1)
            
        for e in e2:
            g2.addEdge(e[0]-1,e[1]-1,10)
        #print(\"g2g\",g2.graph)
        res = g2.KruskalMST()
        #print(\"g2r\",res)
        if len(res) < n - 1:
            return -1
        else:
            print(\"e2\",len(e2),len(e3),n-1)
            ret += len(e2) - (n - 1 - len(e3))
        print(\"g2\",ret)
        
        g1 = Graph(n)
        for e in e3:
            g1.addEdge(e[0]-1,e[1]-1,1)
            
        for e in e1:
            g1.addEdge(e[0]-1,e[1]-1,10)
        res = g1.KruskalMST()
        #print(\"g1r\",res)
        if len(res) < n - 1:
            return -1
        else:
            ret += len(e1) - (n - 1 - len(e3))
        print(\"g1\",ret)
        return ret
        
