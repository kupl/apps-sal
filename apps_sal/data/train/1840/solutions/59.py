# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        longest = [0]

        def dfs(node, d, c):
            if not node:
                longest[0] = max(longest[0], c)
                return

            if d == 'r':
                dfs(node.left, 'l', c + 1)
            else:
                dfs(node.left, 'l', 0)
            if d == 'l':
                dfs(node.right, 'r', c + 1)
            else:
                dfs(node.right, 'r', 0)

        dfs(root, '', 0)
        return longest[0]
