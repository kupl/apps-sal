class Solution:
    def sumOfDistancesInTree(self, N: int, edges: List[List[int]]) -> List[int]:
        tree = [[] for _ in range(N)]
        for i, j in edges:
            tree[i].append(j)
            tree[j].append(i)

        cnt = [1] * N
        res = [0] * N

        def post_order(node, parent):
            for i in tree[node]:
                if i != parent:
                    post_order(i, node)
                    cnt[node] += cnt[i]
                    res[node] += res[i] + cnt[i]

        def pre_order(node, parent):
            for i in tree[node]:
                if i != parent:
                    res[i] = res[node] - cnt[i] + (N - cnt[i])
                    pre_order(i, node)
        post_order(0, -1)
        pre_order(0, -1)

        return res
