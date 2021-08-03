class Solution:
    def sumOfDistancesInTree(self, N: int, edges: List[List[int]]) -> List[int]:
        tree = collections.defaultdict(set)

        for x, y in edges:
            tree[x].add(y)
            tree[y].add(x)

        cnt = [1] * N
        dis = [0] * N

        def predfs(root, pre):
            for k in tree[root]:
                if k != pre:
                    predfs(k, root)
                    cnt[root] += cnt[k]
                    dis[root] += dis[k] + cnt[k]

        def postdfs(root, pre):
            for k in tree[root]:
                if k != pre:
                    dis[k] = dis[root] - 2 * cnt[k] + N
                    postdfs(k, root)

        predfs(0, -1)
        postdfs(0, -1)

        return dis
