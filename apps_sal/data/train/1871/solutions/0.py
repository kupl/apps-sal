# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        self.res = 0

        def helper(node, path_max, path_min):
            if not node:
                return 0
            path_max = max(path_max, node.val)
            path_min = min(path_min, node.val)
            self.res = max(self.res, path_max - path_min)
            helper(node.left, path_max, path_min)
            helper(node.right, path_max, path_min)
        if not root:
            return 0
        helper(root, root.val, root.val)
        return self.res
