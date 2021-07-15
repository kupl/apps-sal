from collections import defaultdict 
class Graph: 
  
    def __init__(self,n:int) -> None: 
        self.V= n 
        self.graph = []
    def addEdge(self,u:int,v:int,w:int)-> None: 
        self.graph.append([u,v,w]) 
    def find(self, parent:List[int], i:int)->int: 
        if parent[i] == i: 
            return i 
        return self.find(parent, parent[i])
    def union(self, parent:List[int], rank:List[int], x:int, y:int)->None: 
        xroot = self.find(parent, x) 
        yroot = self.find(parent, y) 
 
        if rank[xroot] < rank[yroot]: 
            parent[xroot] = yroot 
        elif rank[xroot] > rank[yroot]: 
            parent[yroot] = xroot 
        else : 
            parent[yroot] = xroot 
            rank[xroot] += 1
     
    def KruskalMST(self)->List[List[int]]: 
 
        result =[] 
        i = 0
        e = 0 
        self.graph =  sorted(self.graph,key=lambda item: item[2]) 
  
        parent = []
        rank = [] 
  
        # Create V subsets with single elements 
        for node in range(self.V): 
            parent.append(node) 
            rank.append(0) 
      
        # Number of edges to be taken is equal to V-1 
        while e < self.V -1 : 
  
            # Step 2: Pick the smallest edge and increment  
                    # the index for next iteration 
            u,v,w =  self.graph[i] 
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
  
        return result
                               
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        graph = Graph(n)
        for i in range(n-1):
           point1 = points[i]
           for j in range(i+1,n):
              point2 = points[j]
              manhattan_distance = abs(point1[0]-point2[0]) + abs(point1[1]-point2[1])                
              graph.addEdge(i,j,manhattan_distance)
        ans = 0                       
        for edge in graph.KruskalMST():
           ans += edge[2]
        return ans

