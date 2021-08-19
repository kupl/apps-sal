# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        def helper(root):
            if not root:
                return (-1, -1, -1)
            if not root.left and not root.right:
                return (0, 0, 0)
            else:
                l1, l2, l3 = helper(root.left)
                r1, r2, r3 = helper(root.right)

                return (l3 + 1, max(l3 + 1, r1 + 1, l2, r2), r1 + 1)
        return helper(root)[1]
