# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        if root is None:
            return 0
        self.sol = 0
        
        def recursive_long_zigzag(node):
            if node.left is None and node.right is None:
                return 0,0
            max_left = 0
            max_right = 0
            if node.left:
                _, left_s_right = recursive_long_zigzag(node.left)
                max_left = left_s_right + 1
                self.sol = max(self.sol, max_left)
            if node.right:
                right_s_left, _ = recursive_long_zigzag(node.right)
                max_right = right_s_left + 1
                self.sol = max(self.sol, max_right)
            return max_left, max_right
        
        recursive_long_zigzag(root)
        return self.sol
