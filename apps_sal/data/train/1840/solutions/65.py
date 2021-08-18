class Solution:
    def node_is_on_the_right(self, node):
        if not node:
            return 0
        continuation = 1 + self.node_is_on_the_left(node.left)
        starts_here = self.node_is_on_the_right(node.right)
        self.m = max(self.m, starts_here)
        return continuation

    def node_is_on_the_left(self, node):
        if not node:
            return 0
        continuation = 1 + self.node_is_on_the_right(node.right)
        starts_here = self.node_is_on_the_left(node.left)
        self.m = max(self.m, starts_here)
        return continuation

    def longestZigZag(self, root: TreeNode) -> int:
        self.m = 0

        x = self.node_is_on_the_right(root) - 1
        self.m = max(self.m, x)

        return self.m
