class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:

        def findRoot(node, p):
            if node not in p:
                p[node] = node
                return node
            if p[node] != node:
                p[node] = findRoot(p[node], p)
            return p[node]

        def union(node1, node2, p):
            if findRoot(node1, p) == findRoot(node2, p):
                return 0
            p[findRoot(node1, p)] = findRoot(node2, p)
            return 1

        def checkUnited(p, n):
            root = None
            for node in p:
                if root != None and findRoot(node, p) != root:
                    return False
                root = findRoot(node, p)
            return len(p) == n

        cnt = 0
        p1 = {}
        p2 = {}
        for edge in edges:
            if edge[0] == 3:
                cnt += union(edge[1], edge[2], p1)
                union(edge[1], edge[2], p2)

        for edge in edges:
            if edge[0] == 1:
                cnt += union(edge[1], edge[2], p1)
            if edge[0] == 2:
                cnt += union(edge[1], edge[2], p2)

        return len(edges) - cnt if checkUnited(p1, n) and checkUnited(p2, n) else -1
