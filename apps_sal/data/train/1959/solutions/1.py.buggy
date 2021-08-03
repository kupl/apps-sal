# Definition for a binary tree node.
 # class TreeNode:
 #     def __init__(self, x):
 #         self.val = x
 #         self.left = None
 #         self.right = None
 
 class Solution:
     def minDiffInBST(self, root):
         min_diff = float('inf')
         curr = root
         stack = []
         last_val = float('inf')
         while stack or curr:
             while curr:
                 stack.append(curr)
                 curr = curr.left
                 
             curr = stack.pop()
             min_diff = min(min_diff, abs(curr.val - last_val))
             last_val = curr.val
             curr = curr.right
             
         return min_diff
                 
