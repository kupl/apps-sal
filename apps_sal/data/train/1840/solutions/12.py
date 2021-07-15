# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        def zigzag(node: TreeNode) -> tuple:
            if not node: return 0, 0
            _, lr = zigzag(node.left)
            rl, _ = zigzag(node.right)
            self.max_path = max(self.max_path, lr + 1, rl + 1)
            return lr + 1, rl + 1

        self.max_path = 0
        zigzag(root)
        return self.max_path - 1
