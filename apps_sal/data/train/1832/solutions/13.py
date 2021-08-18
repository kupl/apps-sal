class Solution:

    def reachableNodes(self, edges, M, N):
        graph = defaultdict(dict)
        for u, v, w in edges:
            graph[u][v] = graph[v][u] = w

        heap = [(0, 0)]
        dist = {0: 0}
        used = dict()
        ans = 0

        while heap:
            adist, anode = heapq.heappop(heap)
            if adist > dist[anode]:
                continue

            ans += 1

            for nei, weight in graph[anode].items():
                v = min(weight, M - adist)
                used[(anode, nei)] = v

                adist2 = adist + weight + 1
                if adist2 < dist.get(nei, M + 1):
                    dist[nei] = adist2
                    heapq.heappush(heap, (adist2, nei))
        for u, v, w in edges:
            ans += min(w, used.get((u, v), 0) + used.get((v, u), 0))
        return ans

    def reachableNodes2(self, edges, M, N):
        graph = defaultdict(dict)
        for u, v, w in edges:
            graph[u][v] = graph[v][u] = w

        heap = [(0, 0)]
        dist = {0: 0}
        used = dict()
        ans = 0

        while heap:
            adist, anode = heapq.heappop(heap)
            if adist > dist[anode]:
                continue

            ans += 1

            for nei, weight in graph[anode].items():
                v = min(weight, M - adist)
                used[(anode, nei)] = v

                adist2 = adist + weight + 1
                if adist2 < dist.get(nei, M + 1):
                    dist[nei] = adist2
                    heapq.heappush(heap, (adist2, nei))

        for u, v, weight in edges:
            ans += min(weight, used.get((u, v), 0) + used.get((v, u), 0))
        return ans

    def reachableNodes1(self, edges, M, N):

        e = collections.defaultdict(dict)
        for i, j, l in edges:
            e[i][j] = e[j][i] = l
        pq = [(-M, 0)]
        seen = {}
        while pq:
            moves, i = heapq.heappop(pq)
            if i not in seen:
                seen[i] = -moves
                for j in e[i]:
                    moves2 = -moves - e[i][j] - 1
                    if j not in seen and moves2 >= 0:
                        heapq.heappush(pq, (-moves2, j))
        res = len(seen)
        for i, j, k in edges:
            res += min(seen.get(i, 0) + seen.get(j, 0), e[i][j])
        return res
