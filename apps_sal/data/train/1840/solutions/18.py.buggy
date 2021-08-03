# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        if not root: return
        root.val = 0
        
        result = [0]
        self.zigZagHelper(root.left, \"L\", root.val+1, result)
        self.zigZagHelper(root.right, \"R\", root.val+1, result)
        return result[0]
        
    def zigZagHelper(self, root, prev_dir, prev_val, result):
        if not root: 
            return
        
        root.val = prev_val
        result[0] = max(result[0], root.val)
        
        if prev_dir == \"L\":
            self.zigZagHelper(root.right, \"R\", root.val + 1, result)
            self.zigZagHelper(root.left, \"L\", 1, result)
        else:
            self.zigZagHelper(root.right, \"R\", 1, result)
            self.zigZagHelper(root.left, \"L\", root.val + 1, result)
