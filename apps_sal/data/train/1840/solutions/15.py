# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        def ZigZag(node):  # -> [left_len, right_len, max_len]
            if not node:
                return [-1, -1, -1]
            left = ZigZag(node.left)
            right = ZigZag(node.right)
            return [left[1] + 1, right[0] + 1, max(left[1] + 1, right[0] + 1, left[2], right[2])]
        return ZigZag(root)[-1]
