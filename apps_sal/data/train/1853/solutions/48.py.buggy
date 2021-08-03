import math

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        distance=[[math.inf for i in range(n)] for j in range(n)]
        for i in edges:
            distance[i[0]][i[1]]=i[2]
            distance[i[1]][i[0]]=i[2]
            
        for i in range(n):
            for j in range(n):
                if i!=j and distance[i][j]!=math.inf:
                    for k in range(n):
                        if k!=i:
                            d=distance[i][j]+distance[j][k]
                            if d<distance[i][k]:
                                distance[i][k]=d
                                # print(i,j,k)
                                # print(\"\
\")
                            
        for i in range(n):
            for j in range(n):
                if i!=j and distance[i][j]!=math.inf:
                    for k in range(n):
                        if k!=i:
                            d=distance[i][j]+distance[j][k]
                            if d<distance[i][k]:
                                distance[i][k]=d
                                
        # print(distance)
        mini=math.inf
        for i in range(n):
            a=0
            for j in range(n):
                if distance[i][j]<=distanceThreshold:
                    a+=1
            # print(a)
            if a<=mini:
                mini=a
                city=i
                
        return city
