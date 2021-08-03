class Solution:
    def sumOfDistancesInTree(self, N: int, edges: List[List[int]]) -> List[int]:
        # count the number of childrens
        # compute the distance from other nodes to 0
        def dfs(node, parent):
            for child in graph[node]:
                if child != parent:
                    dfs(child, node)
                    count_self_and_children[node] += count_self_and_children[child]
                    res[node] += res[child] + count_self_and_children[child]

        # compute the res of all nodes except 0
        def dfs2(node, parent):
            for child in graph[node]:
                if child != parent:
                    res[child] = res[node] + N - 2 * count_self_and_children[child]
                    dfs2(child, node)

        graph = collections.defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        count_self_and_children = [1] * N
        # res[x] = x@X+y@Y+#(Y)
        # res[y] = y@Y+x@X+#(X)
        # res[y]-res[x] = #(X)-#(Y)
        # res[y] = res[x]+#(X)-#(Y)
        # #(X) = N-#(Y)
        # res[y] = res[x]+(N-#(Y))-#(Y)
        # res[y] = res[x]+N-2#(Y)
        res = [0] * N
        dfs(0, None)
        dfs2(0, None)

        return res
