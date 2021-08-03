from collections import defaultdict


class Solution:
    def sumOfDistancesInTree(self, N: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(set)
        for e in edges:
            f, t = e[0], e[1]
            graph[f].add(t)
            graph[t].add(f)
        dis = [0 for x in range(N)]
        cnt = [1 for x in range(N)]
        self.getRootDis(0, None, dis, cnt, graph)
        self.updateNei(0, None, dis, cnt, graph, N)
        return dis

    def getRootDis(self, curr, parent, dis, cnt, graph):
        rdis, rcnt = 0, 1
        for nei in graph[curr]:
            if nei == parent:
                continue
            self.getRootDis(nei, curr, dis, cnt, graph)
            rdis += dis[nei] + cnt[nei]
            rcnt += cnt[nei]
        dis[curr], cnt[curr] = rdis, rcnt

    def updateNei(self, curr, parent, dis, cnt, graph, N):
        for nei in graph[curr]:
            if nei == parent:
                continue
            dis[nei] = dis[curr] + N - 2 * cnt[nei]
            self.updateNei(nei, curr, dis, cnt, graph, N)
