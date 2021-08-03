class Solution:
    def sumOfDistancesInTree(self, N: int, edges: List[List[int]]) -> List[int]:

        connect = [set() for _ in range(N)]
        num_children = [0] * N
        dist = [0] * N

        for i, j in edges:
            connect[i].add(j)
            connect[j].add(i)
        dist[0] = self.dfs1(0, connect, num_children, 0, set())

        self.dfs2(0, connect, num_children, dist, 0, N, set())

        return dist

    def dfs1(self, cur, connect, num_children, dist, seen):
        seen.add(cur)
        if not connect[cur]:
            num_children[cur] = 1
            return dist

        total_dist = 0

        for i in connect[cur]:
            if i in seen:
                continue

            total_dist += self.dfs1(i, connect, num_children, dist + 1, seen)
            num_children[cur] += num_children[i]

        num_children[cur] += 1

        return total_dist + dist

    def dfs2(self, cur, connect, num_children, res, previous, N, seen):
        seen.add(cur)

        if cur != 0:
            res[cur] = res[previous] - num_children[cur] + N - num_children[cur]
        for i in connect[cur]:
            if i in seen:
                continue
            self.dfs2(i, connect, num_children, res, cur, N, seen)
