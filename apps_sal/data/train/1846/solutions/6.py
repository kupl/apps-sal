class Solution:

    def pruneTree(self, root: TreeNode) -> TreeNode:
        return self.dfs(root)

    def dfs(self, root):
        if not root:
            return None
        root.left = self.dfs(root.left)
        root.right = self.dfs(root.right)
        if not root.val and (not root.left) and (not root.right):
            return None
        return root
