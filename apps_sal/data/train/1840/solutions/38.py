# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        longest = 0
        if not root:
            return longest
        #direction - right = True, left = False
        def helper(root, level, direction):
            nonlocal longest 
            if level > longest:
                longest = level
            if direction:
                if root.left:
                    helper(root.left, level+1, not direction)
                if root.right:
                    helper(root.right,1,direction)
            else:
                if root.right:
                    helper(root.right, level+1, not direction)
                if root.left:
                    helper(root.left, 1, direction)
            
        if root.right:
            helper(root.right,1,True)
        if root.left:
            helper(root.left,1,False)
        if not root.left and not root.right:
            return 0
        return longest

