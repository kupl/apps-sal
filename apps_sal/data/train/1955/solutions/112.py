class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:

        def find(x):
            parent.setdefault(x, x)
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            px = find(x)
            py = find(y)
            parent[px] = py

        parent = dict()

        for i, j in pairs:
            x = i
            y = j
            px = find(x)
            py = find(y)
            if px != py:
                union(x, y)

        graph = collections.defaultdict(list)

        for i in range(len(s)):
            px = find(i)
            heapq.heappush(graph[px], s[i])

        print(graph)

        res = ''
        mem = collections.defaultdict(int)
        for i in range(len(s)):
            px = find(i)

            res += heapq.heappop(graph[px])
        return res
