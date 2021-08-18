class Solution:

    def pruneTreeHelper(self, root: TreeNode) -> TreeNode:
        if not root:
            return None

        left = self.pruneTreeHelper(root.left)
        right = self.pruneTreeHelper(root.right)

        if not left:
            root.left = None

        if not right:
            root.right = None

        if root.val == 0 and root.right is None and root.left is None:
            return None
        else:
            return root

    def pruneTree(self, root: TreeNode) -> TreeNode:
        return self.pruneTreeHelper(root)
