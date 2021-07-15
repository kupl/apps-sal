class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        paths = []
        for i in range(n): paths.append([sys.maxsize] * n)
        
        # all non edges are inf
        # all self paths are 0
        for src,dest,weight in edges:
            paths[src][dest] = weight
            paths[dest][src] = weight
        for i in range(n): paths[i][i] = 0
      
        # calculate all source shortest paths
        for k in range(n):
            for src in range(n):
                for dest in range(n):
                    paths[src][dest] = min(paths[src][dest], paths[src][k] + paths[k][dest])

        globalNode = -1
        globalReachable = sys.maxsize

        for i in range(n):
            localNode = i
            localReachable = 0
            
            for j in range(n):
                if paths[i][j] <= distanceThreshold and j != i: 
                    localReachable += 1
                
            if localReachable < globalReachable: 
                globalReachable = localReachable
                globalNode = localNode

            elif localReachable == globalReachable and localNode > globalNode:
                globalNode = localNode
                
        return globalNode

