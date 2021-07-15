#minima spanning tree
#greedy add min edge and check cycle
#union group to check cycly

import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def distance(points, i, j) -> int:
            return abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
        
        def getGroup(group, x):
            if group[x] == x: return x
            group[x] = getGroup(group, group[x])
            #print(\"x = {}, group[x] = {}\".format(x, group[x]))
            return group[x]
        
        def isCycle(group, cur):
            g1 = getGroup(group, cur[1])
            g2 = getGroup(group, cur[2])
            #print(\" is Cycle ? g1 = {}, g2 = {}\".format(g1,g2))
            return g1 == g2
        
        def unio(group, cur):
            g1 = getGroup(group, cur[1])
            g2 = getGroup(group, cur[2])
            group[g2] = g1
        
        pq, group = [], []
        n = len(points)
        for i in range(n):
            group.append(i)
            for j in range(i+1, n):
                dis = distance(points, i, j)
                heapq.heappush(pq, (dis, i, j))
                
        #print([heappop(pq) for i in range(len(pq))])
        #print(\"group = \" + str(group))
        count, rtn = 0, 0        
        while count < n-1 :
            cur = heapq.heappop(pq)
            #print(cur)
            
            if not isCycle(group, cur): 
             #   print(\"{} and {}\".format(cur[1], cur[2]))
                unio(group, cur)
                rtn += cur[0]
                count += 1
            
        
        
        return rtn;
    
                    

