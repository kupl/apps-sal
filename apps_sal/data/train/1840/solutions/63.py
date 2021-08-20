class Solution:

    def longestZigZag(self, root: TreeNode) -> int:
        if not root:
            return 0
        if not root.left and (not root.right):
            return 0

        def dfs(root, flag, count):
            if not root:
                self.res = max(self.res, count - 1)
                return
            if flag == 1:
                dfs(root.left, -1, 1 + count)
                dfs(root.right, 1, 1)
            else:
                dfs(root.right, 1, 1 + count)
                dfs(root.left, -1, 1)
        self.res = 0
        dfs(root, -1, 0)
        return self.res
