# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: TreeNode) -> int:

        def help(root):
            if not root:
                return [-1, -1, -1]
            left, right = help(root.left), help(root.right)
            return [left[1] + 1, right[0] + 1, max(left[-1], right[-1], left[1] + 1, right[0] + 1)]

        return help(root)[-1]
