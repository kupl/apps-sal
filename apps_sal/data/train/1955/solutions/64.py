class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:

        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            px = find(x)
            py = find(y)
            parent[px] = py

        parent = list(range(len(s) + 1))

        for x, y in pairs:
            px = find(x)
            py = find(y)
            if px != py:
                union(x, y)

        graph = collections.defaultdict(list)

        for i in range(len(s)):
            px = find(i)
            heapq.heappush(graph[px], s[i])  # We are using priority queue to keep track of the lexicographical ordering

        res = ''
        for i in range(len(s)):
            px = find(i)
            res += heapq.heappop(graph[px])
        return res
