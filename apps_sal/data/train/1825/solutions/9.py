class Solution:

    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        return self.helper(root)[0]

    def helper(self, root):
        if not root:
            return (None, 0)
        (n1, l1) = self.helper(root.left)
        (n2, l2) = self.helper(root.right)
        if l1 > l2:
            return (n1, l1 + 1)
        elif l1 < l2:
            return (n2, l2 + 1)
        else:
            return (root, l1 + 1)
