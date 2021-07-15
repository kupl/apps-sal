class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        '''
        prim's algorithm.
        for each left over points:
                add the shortest edge to the tree.
                update the shortest edge from the left over points.
        '''
        cost = 0
        Left_over_points_minEdge = [(abs(points[i][0]-points[0][0])+abs(points[i][1]-points[0][1]),0,i) for i in range(1,len(points))]
        heapq.heapify(Left_over_points_minEdge)
        #mst = [] # to store the minimal spanning tree. Not necessary here.
        while Left_over_points_minEdge: # K for K in N-1... 1
            shortest, frm, to = heapq.heappop(Left_over_points_minEdge) #(O(1))
            cost += shortest
            #mst.append((frm,to))
            
            # \"add or rather use\" new edges from \"to\" and update the min distance to the tree
            for pos,(d, _, i ) in enumerate( Left_over_points_minEdge ): #O(K-1)
                dist = abs(points[i][0]-points[to][0])+abs(points[i][1]-points[to][1])
                if dist < d:
                    Left_over_points_minEdge[pos] = (dist,to,i)
                    heapq._siftdown(Left_over_points_minEdge,0,pos) #(O(log(K))
            
            #heapq.heapify(Left_over_points_minEdge) #O(K-1)
            
        #print(mst)    
        return cost
            
        
        
        
        
        
                
        
        
        
            

