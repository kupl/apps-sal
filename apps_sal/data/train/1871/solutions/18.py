# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        # O(n) where n is the amount of nodes in tree
        def mdiff(root, maxval, minval):
            if not root:
                return -1
            maxval = max(root.val, maxval)
            minval = min(minval, root.val)
            return max(abs(maxval - minval), mdiff(root.left, maxval, minval), mdiff(root.right, maxval, minval))

        return mdiff(root, 0, 100000)
