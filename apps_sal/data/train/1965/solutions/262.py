class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        graph = [collections.defaultdict(list), collections.defaultdict(list), collections.defaultdict(list)]
        temp = [[], [], []]
        for t, a, b in edges:
            temp[t - 1].append([a, b])

            if t in (1, 3):
                graph[0][a].append(b)
                graph[0][b].append(a)
            if t in (2, 3):
                graph[1][a].append(b)
                graph[1][b].append(a)

        def helper(i):
            que = [1]
            seen = set(que)
            for node in que:
                #print(i, que)
                for y in graph[i][node]:
                    if y not in seen:
                        seen.add(y)
                        que.append(y)

            return len(seen) == n
        if not helper(0) or not helper(1):
            return -1

        p = list(range(n + 1))

        def find(i):
            if p[i] != i:
                p[i] = find(p[i])
            return p[i]

        def union(i, j):
            p[find(i)] = find(j)

        def helper(c):

            ans = 0
            for x, y in c:
                if find(x) == find(y):
                    ans += 1
                else:
                    union(x, y)
            return ans

        res = helper(temp[2])
        old = p[:]
        for c in temp[:2]:
            res += helper(c)
            p = old
        return res
