# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def helper(root, max_val):
            if not root:
                return 0

            ans = 0
            if root.val >= max_val:
                max_val = root.val
                ans += 1
            return ans + helper(root.left, max_val) + helper(root.right, max_val)
        return helper(root, -float('inf'))
