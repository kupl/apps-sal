class Solution:

    def longestZigZag(self, root: TreeNode) -> int:
        self.res = 0

        def dfs(node):
            if not node:
                return (-1, -1)
            (_, r) = dfs(node.left)
            (l, _) = dfs(node.right)
            self.res = max(self.res, r + 1, l + 1)
            return (r + 1, l + 1)
        dfs(root)
        return self.res
