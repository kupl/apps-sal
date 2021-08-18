class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        self.maxval = float('-inf')

        def dfs(node, ans):
            if node:
                if ans:
                    self.maxval = max(self.maxval, abs(max(ans) - node.val))
                    self.maxval = max(self.maxval, abs(min(ans) - node.val))

                dfs(node.left, ans + [node.val])
                dfs(node.right, ans + [node.val])
        dfs(root, [])
        return self.maxval
