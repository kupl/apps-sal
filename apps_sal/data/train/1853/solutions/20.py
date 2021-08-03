def buildGraph(n, edges):
    graph = [[float('inf')] * n for _ in range(n)]
    for e in edges:
        graph[e[0]][e[1]] = e[2]
        graph[e[1]][e[0]] = e[2]

    '''
    Floyed-Warshall algorithm won't work if diagonal values are not set to 
    0 when self loop distance is not given
    '''
    for i in range(n):
        graph[i][i] = 0

    return graph


def floyedWarshalAllPairDist(graph):
    n = len(graph)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                graph[j][k] = min(graph[j][k], graph[j][i] + graph[i][k])


'''
Algorithm: 
1) Measure all pair distance using Floyed Warshal algorithm
2) Find the city with minimum connected cities with atmost threshold distance
'''


class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        '''
        graph = buildGraph(n, edges)
        floyedWarshalAllPairDist(graph)

        min_city = 0
        min_count = float('inf')
        for i in range(n):
            count = sum([1 if x<=distanceThreshold else 0 for x in graph[i]])
            if count <= min_count:
                min_count = count
                min_city = i

        return min_city
        '''
        g = [[float('inf')] * n for _ in range(n)]
        for u, v, w in edges:
            g[u][v] = w
            g[v][u] = w

        for i in range(n):
            for u in range(n):
                for v in range(n):
                    if u == v:
                        g[u][v] = 0
                    else:
                        g[u][v] = min(g[u][v], g[u][i] + g[i][v])

        city, count = -1, float('inf')
        for i in range(n):
            tmp = sum(1 for x in g[i] if x <= distanceThreshold)
            if tmp <= count:
                city = i
                count = tmp

        return city
