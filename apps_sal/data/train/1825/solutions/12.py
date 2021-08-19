from collections import defaultdict


class Solution:

    def __init__(self):
        self.deepest = -1
        self.m = defaultdict(list)

    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        self.dfs(root, 0)
        if self.deepest == -1:
            return None
        if len(self.m[self.deepest]) == 1:
            return self.m[self.deepest][0]
        return self.lca(root, self.m[self.deepest])

    def dfs(self, node, level):
        if node is None:
            return
        if level not in self.m:
            self.m[level] = []
        self.deepest = max(self.deepest, level)
        self.m[level].append(node)
        self.dfs(node.left, level + 1)
        self.dfs(node.right, level + 1)

    def lca(self, x, nodes):
        if x is None:
            return x
        for node in nodes:
            if node == x:
                return x
        left = self.lca(x.left, nodes)
        right = self.lca(x.right, nodes)
        if left is not None and right is not None:
            return x
        return left if left is not None else right
