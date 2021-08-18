class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        edges = sorted(edges, key=lambda k: k[0], reverse=True)

        A_ranks, B_ranks = [i for i in range(n + 1)], [i for i in range(n + 1)]

        def find(x, ranks):
            if ranks[x] != x:
                ranks[x] = find(ranks[x], ranks)
            return ranks[x]

        def union(x, y, ranks):
            rk_x, rk_y = find(x, ranks), find(y, ranks)
            if rk_x < rk_y:
                ranks[rk_y] = rk_x
            elif rk_y < rk_x:
                ranks[rk_x] = rk_y

        steps, e_A, e_B = 0, 0, 0
        for i in range(len(edges)):
            c, x, y = edges[i]
            if c == 3:
                A_x, A_y, B_x, B_y = find(x, A_ranks), find(y, A_ranks), find(x, B_ranks), find(y, B_ranks)
                if A_x != A_y or B_x != B_y:
                    union(x, y, A_ranks)
                    union(x, y, B_ranks)
                    e_A, e_B = e_A + 1, e_B + 1
                else:
                    steps += 1
        for i in range(len(edges)):
            c, x, y = edges[i]
            if c == 2:
                B_x, B_y = find(x, B_ranks), find(y, B_ranks)
                if B_x != B_y:
                    union(x, y, B_ranks)
                    e_B += 1
                else:
                    steps += 1
        for i in range(len(edges)):
            c, x, y = edges[i]
            if c == 1:
                A_x, A_y = find(x, A_ranks), find(y, A_ranks)
                if A_x != A_y:
                    union(x, y, A_ranks)
                    e_A += 1
                else:
                    steps += 1

        for i in range(1, n + 1):
            find(i, A_ranks)
            find(i, B_ranks)
        print(A_ranks, B_ranks)

        return steps if e_A == e_B == n - 1 else -1
