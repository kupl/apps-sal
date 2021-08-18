class Solution:
    def sumOfDistancesInTree(self, N: int, edges: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        count = [1] * N
        ans = [0] * N
        print(graph)

        def postorder(node=0, parent=None):
            for child in graph[node]:
                if child != parent:
                    postorder(child, node)
                    count[node] += count[child]
                    ans[node] += ans[child] + count[child]

        def preorder(node=0, parent=None):
            for child in graph[node]:
                if child != parent:
                    ans[child] = ans[node] - count[child] + (N - count[child])
                    preorder(child, node)
        postorder()
        preorder()
        return ans
