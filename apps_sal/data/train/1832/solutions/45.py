class Solution:
    def reachableNodes(self, edges: List[List[int]], M: int, N: int) -> int:
        if M == 0: return 1
        graph = [[-1]*N for i in range(N)]
        nodes = set()
        for i,j,n in edges:
            graph[i][j] = n
            graph[j][i] = n
            nodes.add(i)
            nodes.add(j)
        visited = [False]*N
        q = [(-M, 0)]
        cost = 0
        count = 0
        while q:
            cur = heappop(q)
            if count == len(nodes) + 1: break
            if visited[cur[1]]: continue
            count += 1
            visited[cur[1]] = True
            steps = -cur[0]
            cost += 1
            if steps <= 0: continue
            for i in range(N):
                if graph[cur[1]][i] == -1: continue
                adj = (graph[cur[1]][i], i)
                if adj[0] + 1 > steps:
                    cost += steps
                    graph[cur[1]][i] -= steps
                    graph[i][cur[1]] -= steps
                else:
                    cost += adj[0]
                    heappush(q,(-(steps-adj[0]-1), adj[1]))
                    graph[cur[1]][adj[1]] = -1
                    graph[adj[1]][cur[1]] = -1
        return cost
