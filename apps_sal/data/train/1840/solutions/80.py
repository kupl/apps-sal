class Solution:

    def longestZigZag(self, root: TreeNode) -> int:

        def dfs(node):
            if not node.left and (not node.right):
                return (0, 0)
            left = right = 0
            if node.left:
                left = dfs(node.left)[1] + 1
            if node.right:
                right = dfs(node.right)[0] + 1
            self.res = max(self.res, max(left, right))
            return (left, right)
        self.res = 0
        dfs(root)
        return self.res
