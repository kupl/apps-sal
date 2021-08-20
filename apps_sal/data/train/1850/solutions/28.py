from collections import deque


class Node:

    def __init__(self, val):
        self.val = val
        self.size = 0
        self.dist = 0
        self.children = []
        self.parent = None


class Solution:

    def dfsPostorder(self, root):
        if root is None:
            return
        for c in root.children:
            self.dfsPostorder(c)
        size = 0
        dist = 0
        for c in root.children:
            size += c.size
            dist += c.dist
        root.size = size + 1
        root.dist = size + dist

    def dfsPreorder(self, root):
        if root is None:
            return
        if root.parent is not None:
            root.dist = root.parent.dist - 2 * root.size + root.parent.size
            root.size = root.parent.size
        for c in root.children:
            self.dfsPreorder(c)

    def buildTree(self, graph, root, nodes):
        queue = deque()
        queue.append((root, None))
        while len(queue) > 0:
            (cur, par) = queue.pop()
            node = nodes[cur]
            for n in graph[cur]:
                if n != par:
                    node.children.append(nodes[n])
                    nodes[n].parent = node
                    queue.append((n, cur))

    def sumOfDistancesInTree(self, N: int, edges: List[List[int]]) -> List[int]:
        nodes = {i: Node(i) for i in range(N)}
        graph = {i: [] for i in range(N)}
        for (u, v) in edges:
            graph[u].append(v)
            graph[v].append(u)
        root = 0
        self.buildTree(graph, root, nodes)
        root = nodes[root]
        self.dfsPostorder(root)
        self.dfsPreorder(root)
        ans = []
        for i in range(N):
            ans.append(nodes[i].dist)
        return ans
