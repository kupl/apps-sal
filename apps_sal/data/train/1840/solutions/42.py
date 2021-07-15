# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        self.zigzag(root)
        return self.find_longest(root)
    
    def zigzag(self, node: TreeNode) -> int:
        if node is None:
            return
        self.zigzag(node.left)
        self.zigzag(node.right)
        
        if node.left is not None:
            node.left_depth = node.left.right_depth + 1
        else:
            node.left_depth = 0
            
        if node.right is not None:
            node.right_depth = node.right.left_depth + 1
        else:
            node.right_depth = 0
            
    def find_longest(self, node: TreeNode) -> int:
        if node is None:
            return 0
        left_max = self.find_longest(node.left)
        right_max = self.find_longest(node.right)
        return max(left_max, right_max, node.left_depth, node.right_depth)
