"""
Created on Fri Feb 21 15:46:01 2020

@author: pramo
"""
import resource
import sys
resource.setrlimit(resource.RLIMIT_STACK, (2 ** 29, -1))
sys.setrecursionlimit(10 ** 6)


class graph:
    """docstring for graph"""

    def __init__(self, N):
        self.N = N
        self.adjacent_list = [[] for i in range(N)]

    def add_road(self, a, b):
        self.adjacent_list[a].append(b)
        self.adjacent_list[b].append(a)

    def DFS_iterate(self, con_list, n, visited):
        visited[n] = True
        con_list.append(n)
        for i in self.adjacent_list[n]:
            if visited[i] == False:
                con_list = self.DFS_iterate(con_list, i, visited)
        return con_list

    def connected_groups(self):
        visited = [False for i in range(N)]
        con_groups = []
        for n in range(N):
            if visited[n] == False:
                con_list = []
                con_groups.append(self.DFS_iterate(con_list, n, visited))
        return con_groups


T = int(input())
for x in range(T):
    (N, M, K) = list(map(int, input().split()))
    city_map = graph(N)
    for i in range(M):
        road = list(map(int, input().split()))
        city_map.add_road(road[0] - 1, road[1] - 1)
    museums_city = list(map(int, input().split()))
    con_groups = city_map.connected_groups()
    if len(con_groups) < K:
        print('-1')
    else:
        museums_groups = []
        for group in con_groups:
            museums_group = 0
            for city in group:
                museums_group += museums_city[city]
            museums_groups.append(museums_group)
        total_museums = 0
        museums_groups.sort(reverse=True)
        Ladki = 0
        Nikhil = len(museums_groups) - 1
        for j in range(K):
            if j % 2 == 0:
                total_museums += museums_groups[Ladki]
                Ladki += 1
            else:
                total_museums += museums_groups[Nikhil]
                Nikhil -= 1
        print(total_museums)
