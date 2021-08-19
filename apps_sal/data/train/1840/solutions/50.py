# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: TreeNode) -> int:

        self.max = 0

        def dfs(node):
            if not node:
                return -1, -1

            l_dir_left, l_dir_right = dfs(node.left)
            r_dir_left, r_dir_right = dfs(node.right)
            self.max = max(self.max, l_dir_left, l_dir_right + 1, r_dir_left + 1, r_dir_right)
            return (l_dir_right + 1, r_dir_left + 1)

        dfs(root)
        return self.max
