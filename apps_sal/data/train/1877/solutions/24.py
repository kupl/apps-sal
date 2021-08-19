# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, root, total, limit):
        if not root:
            return False

        if root.left == None and root.right == None:
            return total + root.val >= limit

        left = self.helper(root.left, total + root.val, limit)
        right = self.helper(root.right, total + root.val, limit)

        if not left:
            root.left = None
        if not right:
            root.right = None

        return left or right

    def sufficientSubset(self, root: TreeNode, limit: int) -> TreeNode:
        if self.helper(root, 0, limit):
            return root
        else:
            return None
