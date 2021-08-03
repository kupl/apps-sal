class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:

        dist = [[math.inf] * n for _ in range(n)]
        for i, j, w in edges:
            dist[i][j] = w
            dist[j][i] = w

        for i in range(n):
            dist[i][i] = 0

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

        res = []
        for i in range(n):
            res.append(sum(dist[i][j] <= distanceThreshold for j in range(n)))

        print(res)

        tmp = (n, 0)
        for i, c in enumerate(res):
            # print(tmp)
            if (c, -i) < tmp:
                tmp = (c, -i)

        return -tmp[1]


#         graph = collections.defaultdict(list)
#         for i,j,w in edges:
#             graph[i].append([j,w])
#             graph[j].append( [i, w] )


#         res = [0]*n

#         for i in range(n):
#             print('start')
#             print(i)
#             visited = set([i])
#             que = collections.deque([ (i,0) ])
#             while que:
#                 cur, dist = que.popleft()
#                 for j,w in graph[cur]:
#                     print([j, dist+w] )
#                     if j not in visited and dist+w<=distanceThreshold:

#                         visited.add(j)
#                         que.append( [j,dist+w ] )
#                         res[i]+=1

#         # print(res)

#         m = min(res)
#         for i in range(n-1, -1, -1):
#             if res[i] == m:
#                 return i
