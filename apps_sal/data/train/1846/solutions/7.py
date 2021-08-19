class Solution:

    def pruneTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        l = self.pruneTree(root.left)
        r = self.pruneTree(root.right)
        if not l and (not r) and (root.val == 0):
            return None
        root.left = l
        root.right = r
        return root
