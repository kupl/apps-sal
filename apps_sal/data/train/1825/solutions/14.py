
class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        def height(root):
            if not root:
                return 0
            return 1 + max(height(root.left), height(root.right))
        if height(root.left) == height(root.right):
            return root
        elif height(root.left) > height(root.right):
            return self.lcaDeepestLeaves(root.left)
        return self.lcaDeepestLeaves(root.right)
