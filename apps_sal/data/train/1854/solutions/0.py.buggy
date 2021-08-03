# Definition for a binary tree node.
 # class TreeNode:
 #     def __init__(self, x):
 #         self.val = x
 #         self.left = None
 #         self.right = None
 
 class Solution:
     def rob(self, root):
         """
         :type root: TreeNode
         :rtype: int
         """
         def superrob(node):
             # returns tuple of size two (now, later)
             # now: max money earned if input node is robbed
             # later: max money earned if input node is not robbed
 
             # base case
             if not node: return (0, 0)
 
             # get values
             left, right = superrob(node.left), superrob(node.right)
 
             # rob now
             now = node.val + left[1] + right[1]
 
             # rob later
             later = max(left) + max(right)
 
             return (now, later)
 
         return max(superrob(root))

