class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        graph = [list() for i in range(N)]
        for dislike in dislikes:
            x = dislike[0]
            y = dislike[1]
            graph[x - 1].append(y - 1)
            graph[y - 1].append(x - 1)

        parent = list(range(N))

        def find(p):
            if p != parent[p]:
                parent[p] = find(parent[p])
            return parent[p]

        def union(p, q):
            pr = find(p)
            qr = find(q)
            if pr != qr:
                parent[pr] = qr
            return

        for i in range(N):
            if not graph[i]:
                continue
            x = find(i)
            y = find(graph[i][0])
            if x == y:
                return False
            for j in range(1, len(graph[i])):
                z = find(graph[i][j])
                if z == x:
                    return False
                union(y, z)

        return True
