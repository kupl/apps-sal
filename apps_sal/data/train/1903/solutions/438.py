class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        def minnode(n, keyval, mstset): 
            mini = 999999999999
            mini_index = None

            # Loop through all the values of  
            # the nodes which are not yet  
            # included in MST and find the  
            # minimum valued one. 
            for i in range(n): 
                if (mstset[i] == False and 
                    keyval[i] < mini):  
                    mini = keyval[i] 
                    mini_index = i 
            return mini_index 
        
        
        def findcost(n, city): 
  
            # Array to store the parent  
            # node of a particular node.  
            parent = [None] * n 

            # Array to store key value  
            # of each node.  
            keyval = [None] * n  

            # Boolean Array to hold bool  
            # values whether a node is 
            # included in MST or not.  
            mstset = [None] * n 

            # Set all the key values to infinite and  
            # none of the nodes is included in MST. 
            for i in range(n): 
                keyval[i] = 9999999999999
                mstset[i] = False

            # Start to find the MST from node 0.  
            # Parent of node 0 is none so set -1.  
            # key value or minimum cost to reach  
            # 0th node from 0th node is 0.  
            parent[0] = -1
            keyval[0] = 0

            # Find the rest n-1 nodes of MST. 
            for i in range(n - 1): 

                # First find out the minimum node  
                # among the nodes which are not yet  
                # included in MST.  
                u = minnode(n, keyval, mstset)  

                # Now the uth node is included in MST.  
                mstset[u] = True

                # Update the values of neighbor  
                # nodes of u which are not yet  
                # included in MST.  
                for v in range(n): 
                    if (city[u][v] and mstset[v] == False and 
                        city[u][v] < keyval[v]):  
                        keyval[v] = city[u][v]  
                        parent[v] = u 

            # Find out the cost by adding  
            # the edge values of MST.  
            cost = 0
            for i in range(1, n): 
                cost += city[parent[i]][i]  
            return cost
    
        n = len(points)
        city = [[0 for c in range(n)] for r in range(n)]
        
        for r in range(n):
            c1 = points[r]
            for c in range(n):
                c2 = points[c]
                
                val = abs(points[r][0] - points[c][0]) + abs(points[r][1] - points[c][1])
                city[r][c] = val
        
        return findcost(n, city)
        
        
        

