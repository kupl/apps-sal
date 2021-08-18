class Solution:
    def longestZigZag(self, root: TreeNode) -> int:

        self.res = 0

        def dfs(node):
            if not node:
                return -1, -1
            else:
                left = dfs(node.left)
                right = dfs(node.right)
                self.res = max(self.res, 1 + max(left[1], right[0]))
                return 1 + left[1], 1 + right[0]
        dfs(root)
        return self.res
