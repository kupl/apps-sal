from bisect import insort
from copy import copy


class Solution:

    def traverse(self, root, path=[]):
        if root is None:
            return
        path = copy(path)
        insort(path, root.val)
        if root.left is None and root.right is None:
            path_abs_diff = path[-1] - path[0]
            self.max_abs_diff = max(self.max_abs_diff, path_abs_diff)
        self.traverse(root.left, path)
        self.traverse(root.right, path)

    def maxAncestorDiff(self, root: TreeNode) -> int:
        self.max_abs_diff = 0
        self.traverse(root)
        return self.max_abs_diff
