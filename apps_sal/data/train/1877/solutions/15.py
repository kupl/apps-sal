class Solution:
    def sufficientSubset(self, root: TreeNode, limit: int) -> TreeNode:

        if not root:
            return root
        if not root.left and not root.right:
            return root if root.val >= limit else None

        root.left = self.sufficientSubset(root.left, limit - root.val)
        root.right = self.sufficientSubset(root.right, limit - root.val)

        return root if root.left or root.right else None
