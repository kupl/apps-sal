from collections import defaultdict
class Solution:
    def sumOfDistancesInTree(self, N: int, edges: List[List[int]]) -> List[int]:
        dd = defaultdict(set)
        # 将edges中的路径构建成树
        for u, v in edges:
            dd[u].add(v)
            dd[v].add(u)
        # 这题核心需要关注的两种数据分别为当前节点有多少个子节点（包含自己）以及当前节点到所有子节点的路径距离和
        counts = [1] * N # 记录当前节点有多少个子节点（包括自己）
        dists = [0] * N # 记录当前节点到子节点的路径距离之和
        # 以0为root的情况下counts和dists
        def dfs1(root, pre):
            for node in dd[root]:
                if node != pre:
                    dfs1(node, root)
                    counts[root] += counts[node]
                    dists[root] += dists[node] + counts[node]
        # 调整root位置到各个节点，同时更新dists；这里的计算原理是，root移动到node，同时node下有x个子节点（包括node自己），
        # 那么就是与x个节点的距离-1，同时与N-x个节点的距离+1
        def dfs2(root, pre):
            for node in dd[root]:
                if node != pre:
                    dists[node] = dists[root] - 1*counts[node] + 1*(N - counts[node])
                    dfs2(node, root)
        dfs1(0, -1)
        dfs2(0, -1)
        return dists
