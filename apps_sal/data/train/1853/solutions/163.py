class Solution:

    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        h = collections.defaultdict(list)
        for i in edges:
            h[i[0]].append((i[1], i[2]))
            h[i[1]].append((i[0], i[2]))
        c = 0
        no = 101
        for i in range(n):
            b = set()
            q = []
            heapq.heappush(q, (0, i, -1))
            while q:
                x = heapq.heappop(q)
                if x[1] in b:
                    continue
                b.add(x[1])
                for j in h[x[1]]:
                    if j[1] + x[0] <= distanceThreshold and j[0] != x[2] and (j[0] not in b):
                        heapq.heappush(q, (j[1] + x[0], j[0], x[1]))
            if len(b) - 1 <= no:
                no = len(b) - 1
                c = i
                print(len(b) - 1)
        return c
