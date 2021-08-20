class Solution:

    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        g = {}
        for (u, v, w) in edges:
            if u in g:
                g[u].append((v, w))
            else:
                g[u] = [(v, w)]
            if v in g:
                g[v].append((u, w))
            else:
                g[v] = [(u, w)]

        def numOfNb(city):
            minheap = [(0, city)]
            dist = {}
            while minheap:
                (currw, u) = heapq.heappop(minheap)
                if u != city:
                    dist[u] = currw
                if u not in g:
                    continue
                for (v, w) in g[u]:
                    if v in dist:
                        continue
                    if currw + w <= distanceThreshold:
                        heapq.heappush(minheap, (currw + w, v))
            return len(dist)
        ans = 0
        minnb = n
        for i in range(n):
            nb = numOfNb(i)
            if nb <= minnb:
                minnb = nb
                ans = i
        return ans
