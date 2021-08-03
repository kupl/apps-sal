# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        self.ans = 0

        def preorder(root, minval, maxval):
            if not root:
                self.ans = max(self.ans, abs(minval - maxval))
                return

            preorder(root.left, min(minval, root.val), max(maxval, root.val))
            preorder(root.right, min(minval, root.val), max(maxval, root.val))

        preorder(root, float('inf'), float('-inf'))
        return self.ans
