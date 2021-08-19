class Solution:

    def sumOfDistancesInTree(self, N: int, edges: List[List[int]]) -> List[int]:
        Nodes = [None] * N

        def node(i):
            if Nodes[i] is None:
                Nodes[i] = Node(i)
            return Nodes[i]
        adj = defaultdict(list)
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
        root = node(0)
        stack = [0]
        while stack:
            i = stack.pop()
            for j in adj[i]:
                if Nodes[j] is None:
                    stack.append(j)
                    node(i).children.append(node(j))
        self.below(root)
        ans = [0] * N
        ans[0] = node(0).dists_below
        stack = [node(0)]
        while stack:
            parent = stack.pop()
            for child in parent.children:
                stack.append(child)
                ans[child.val] = ans[parent.val] + N - 2 - 2 * child.below
        return ans

    def below(self, node):
        node.below = 0
        node.dists_below = 0
        for child in node.children:
            self.below(child)
            node.below += 1 + child.below
            node.dists_below += child.dists_below
        node.dists_below += node.below


class Node:

    def __init__(self, val, children=None):
        self.val = val
        self.children = children if children else []
