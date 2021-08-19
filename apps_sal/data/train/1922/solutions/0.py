class Solution:

    def minCameraCover(self, root: TreeNode) -> int:

        def dfs(node):
            if not node:
                return 2
            left = dfs(node.left)
            right = dfs(node.right)
            if left == 0 or right == 0:
                self.res += 1
                return 1
            if left == 1 or right == 1:
                return 2
            else:
                return 0
        self.res = 0
        return (dfs(root) == 0) + self.res
