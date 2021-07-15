# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    m = 0
    def longestZigZag(self, root: TreeNode) -> int:
        def longest(node: TreeNode, state: int, acc: int) -> int:
            self.m = max(self.m, acc)
            if not node:
                return 0
            if state == 0:
                longest(node.right, 1, acc + 1), longest(node.left, 0, 0)
            else:
                longest(node.left, 0, acc + 1), longest(node.right, 1, 0)
            
        longest(root.left, 0, 0), longest(root.right, 1, 0)
        return self.m
