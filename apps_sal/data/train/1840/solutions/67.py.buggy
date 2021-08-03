# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        if not root:
            return 0

        res = 0
        def dfs(root, direction, step):
            nonlocal res
            if not root:
                return

            if direction == \"l\":
                dfs(root.left, 'r', step + 1)
                dfs(root.right, 'l', 1)
            else:
                dfs(root.right, 'l', step + 1)
                dfs(root.left, 'r', 1)
            res = max(res, step)

        dfs(root, 'l', 0)
        dfs(root, 'r', 0)
        return res
