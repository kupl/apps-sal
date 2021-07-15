# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        # Use DFS, and a max diff tracker.
        # Each node has a min-max ancestor.
        # Time: O(N), Space: O(log(N))
        self.max_p_diff = 0
        def max_diff(node, p_min, p_max):
            if not node:
                return
            self.max_p_diff = max(self.max_p_diff, max(abs(node.val-p_min), abs(p_max-node.val)))
            p_min = min(node.val, p_min)
            p_max = max(node.val, p_max)
            max_diff(node.left, p_min, p_max)
            max_diff(node.right, p_min, p_max)
        max_diff(root, root.val, root.val)
        return self.max_p_diff

