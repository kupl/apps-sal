class Solution:

    def traverse(self, root, path=[]):
        if root is None:
            return

        path = path + [root.val]

        if root.left is None and root.right is None:
            path_abs_diff = max(path) - min(path)
            self.max_abs_diff = max(self.max_abs_diff, path_abs_diff)
        elif root.left is None:
            self.traverse(root.right, path)
        elif root.right is None:
            self.traverse(root.left, path)
        else:
            self.traverse(root.left, path)
            self.traverse(root.right, path)

    def maxAncestorDiff(self, root: TreeNode) -> int:
        self.max_abs_diff = 0

        self.traverse(root)

        return self.max_abs_diff
