# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Think: For each subtree, find the minimum value and maximum value of its descendants.
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        self.res = 0

        def helper(node, max_val, min_val):
            # think: we use the recursive way to traverse through the tree.
            if not node:
                self.res = max(self.res, max_val - min_val)
                return
            helper(node.left, max(max_val, node.val), min(min_val, node.val))
            helper(node.right, max(max_val, node.val), min(min_val, node.val))
        helper(root, 0, 100000)
        return self.res
