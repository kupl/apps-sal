class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        self.dist = 0

        def dfs(node, ancesVal):
            if not node:
                self.dist = max(self.dist, abs(max(ancesVal) - min(ancesVal)))
                return

            dfs(node.left, ancesVal + [node.val])

            dfs(node.right, ancesVal + [node.val])
            return

        dfs(root, [])
        return self.dist
