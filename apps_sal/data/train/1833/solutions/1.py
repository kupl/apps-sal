# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        def helper(root):
            if not root:
                return None, 0
            left, h_l = helper(root.left)
            right, h_r = helper(root.right)
            if h_l == h_r:
                return root, h_l + 1
            return (left, h_l + 1) if h_l > h_r else (right, h_r + 1)
        node, _ = helper(root)
        return node
