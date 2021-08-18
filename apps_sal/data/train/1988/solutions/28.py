class Solution:
    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:

        distance = [[float('inf'), float('inf')] for _ in range(n)]
        distance[0][0] = 0
        distance[0][1] = 0

        for _ in range(n):
            for u, v in red_edges:
                if distance[u][1] + 1 < distance[v][0]:
                    distance[v][0] = distance[u][1] + 1
            for u, v in blue_edges:
                if distance[u][0] + 1 < distance[v][1]:
                    distance[v][1] = distance[u][0] + 1

        min_distance = []
        for d in distance:
            min_d = min(d)
            if min_d < float('inf'):
                min_distance.append(min_d)
            else:
                min_distance.append(-1)
        return min_distance


'''

distance[X][0] distance upto X with last edge red
distance[X][1]                      last edge blue



'''
