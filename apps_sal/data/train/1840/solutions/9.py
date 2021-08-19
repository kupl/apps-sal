# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        self.res = float(-inf)

        def helper(root, left, right):
            self.res = max(self.res, max(left, right))
            if root == None:
                return
            if root.left:
                helper(root.left, right + 1, 0)
            if root.right:
                helper(root.right, 0, left + 1)
            return

        helper(root, 0, 0)
        return self.res
