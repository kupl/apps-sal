class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        return root if self.dfs(root) else None

    def dfs(self, root):
        if not root:
            return False
        l = self.dfs(root.left)
        r = self.dfs(root.right)
        if not l:
            root.left = None
        if not r:
            root.right = None
        return root.val == 1 or l or r
