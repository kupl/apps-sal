class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        self.max_diff = -float('inf')
        self.dfs(root, [])
        return self.max_diff

    def dfs(self, root, path):
        if not root:
            # print(path)
            self.max_diff = max(self.max_diff, max(path) - min(path))
            return
        self.dfs(root.left, path + [root.val])
        self.dfs(root.right, path + [root.val])
